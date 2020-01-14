'''
FetcherResponse will return a well-formed FetcherResponse object

    {
        name: string,
        payload: {file_name: binary_data} | None,
        source: string
        error: Error object
    }

    "payload" - string - binary data from a successful url fetch or None on fail
    "source" - string - the url the fetch was performed against
    "error" - error / string - None or the __repr__ of the error on fail
'''


class FetcherResponse:

    name = ''
    source = ''
    payload = None
    error = None

    def __init__(self, name, payload, source, error):
        self.name = name
        self.payload = payload
        self.source = source
        self.error = error

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            'name': self.name,
            'payload': self.payload,
            'source': self.source,
            'error': self.error
        }
