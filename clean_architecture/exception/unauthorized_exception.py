from .exception import BasicException


class UnauthorizedException(BasicException):

    def __init__(self, error_code, message):
        BasicException.__init__(self)
        self.status_code = 401
        self.error_code = error_code
        self.message = message
