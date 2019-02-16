from .exception import BasicException


class NotFoundException(BasicException):

    def __init__(self, message):
        BasicException.__init__(self)
        self.status_code = 404
        self.message = message
