class Result:
    def __init__(self, code, message, data):
        self.code = code
        self.message = message
        self.data = data

    def to_dict(self):
        return {
            'code': self.code,
            'message': self.message,
            'data': self.data
        }

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self.to_dict())

    def __eq__(self, other):
        return self.code == other.code and self.message == other.message and self.data == other.data

    def __ne__(self, other):
        return not self.__eq__(other)


def success(code=1, message=None, data=None):
    return Result(code, message, data)


def error(code=-1, message=None, data=None):
    return Result(code, message, data)

