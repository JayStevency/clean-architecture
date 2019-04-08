from .exception import BasicException


class ConflictedException(BasicException):

    def __init__(self, error_code, message):
        BasicException.__init__(self)
        self.status_code = 409
        self.error_code = error_code
        self.message = message
