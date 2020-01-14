from etl.utils import decompress, get_file_ext
import zipfile


class Parser:
    def flatten(self, response, extensions=None):
        for payload in response.payload:
            if zipfile.is_zipfile(payload.data):
                response.payload = decompress(
                    payload.data, extensions)
                self.flatten(response)
        return response.payload
