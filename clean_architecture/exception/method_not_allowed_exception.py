from .exception import BasicException


class MethodNotAllowedException(BasicException):

    def __init__(self, message):
        BasicException.__init__(self)
        self.status_code = 405
        self.message = message
