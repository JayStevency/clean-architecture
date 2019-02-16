from .exception import BasicException


class NotAcceptableException(BasicException):

    def __init__(self, message):
        BasicException.__init__(self)
        self.status_code = 406
        self.message = message
