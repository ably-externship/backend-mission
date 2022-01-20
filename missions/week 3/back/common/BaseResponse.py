
class BaseResponse:
    def __init__(self, data=None, code=None, message=None):
        self.data = data
        self.code = code
        self.message = message

    def to_dict(self):
        return {
            "code": self.code,
            "message": self.message,
            "data": self.data
        }
