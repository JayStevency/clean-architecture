from .exception import BasicException


class UnauthorizedException(BasicException):

    def __init__(self, message):
        BasicException.__init__(self)
        self.status_code = 401
        self.message = message
