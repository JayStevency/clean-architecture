from .exception import BasicException


class BadRequestException(BasicException):

    def __init__(self, message):
        BasicException.__init__(self)
        self.status_code = 400
        self.message = message
