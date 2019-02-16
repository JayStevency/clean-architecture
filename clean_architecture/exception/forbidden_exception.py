from .exception import BasicException


class ForbiddenException(BasicException):

    def __init__(self, message):
        BasicException.__init__(self)
        self.status_code = 403
        self.message = message
