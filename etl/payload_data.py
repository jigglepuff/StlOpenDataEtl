'''
PayloadData will return a valid object representing the data in a payload

    {
        filename: string,
        data: binary | None
    }
    
'''


class PayloadData:

    filename = ''
    data = None

    def __init__(self, filename, data):
        self.filename = filename
        self.data = data

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            'filename': self.filename,
            'data': self.data
        }
