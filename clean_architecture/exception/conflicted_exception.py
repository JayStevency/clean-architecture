from .exception import BasicException


class ConflictedException(BasicException):

    def __init__(self, message):
        BasicException.__init__(self)
        self.status_code = 409
        self.message = message
