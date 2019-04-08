from .exception import BasicException


class MethodNotAllowedException(BasicException):

    def __init__(self, error_code=None, message=''):
        BasicException.__init__(self)
        self.status_code = 405
        self.error_code = error_code
        self.message = message
