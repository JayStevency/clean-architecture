from .exception import BasicException


class PreconditionFailedException(BasicException):

    def __init__(self, message):
        BasicException.__init__(self)
        self.status_code = 412
        self.message = message
