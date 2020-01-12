#!/usr/bin/env python3

import os
import ssl
import sys
import yaml
from app import ROOT_DIR
from io import BytesIO
from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import URLError


class Fetcher:

    def fetch_all(self, src_yaml):
        '''
        Returns a list of fetcher data objects as defined below. 
        '''
        data = []
        for key in src_yaml.keys():
            data.append(self.fetch(key, src_yaml[key]['url']))

        return data

    def fetch(self, name, url):
        '''
        Returns a fetcher data object.

        Arguments: 
        name -- a friendly name for a given source
        url -- the url from which the fetcher will attempt to fetch

        {
            name: string,
            payload: binary_data | None,
            source: string
            error: Error object
        }

        "payload" - string - binary data from a successful url fetch or None on fail
        "source" - string - the url the fetch was performed against
        "error" - error / string - None or the __repr__ of the error on fail
        '''
        try:
            # start hack - ignoring SSL completely - see https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error
            ssl_context = ssl._create_unverified_context()
            response = urlopen(url, context=ssl_context)
            # end hack
            return {
                'name': name,
                'payload': BytesIO(response.read()),
                'source': url,
                'error': None
            }

        except URLError as url_error:
            return {
                'name': name,
                'payload': None,
                'source': url,
                'error': url_error
            }

        return {
            'name': name,
            'payload': None,
            'source': url,
            'error': 'An error has occurred.'
        }
