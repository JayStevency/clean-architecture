from .exception import BasicException


class ForbiddenException(BasicException):

    def __init__(self, error_code=None, message=''):
        BasicException.__init__(self)
        self.status_code = 403
        self.error_code = error_code
        self.message = message
