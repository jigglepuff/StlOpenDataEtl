import os
from etl import fetcher, parser
from etl import utils

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    fetcher = fetcher.Fetcher()
    src_yaml = utils.get_yaml('data/sources/sources.yml')
    result = fetcher.fetch_all(src_yaml)
