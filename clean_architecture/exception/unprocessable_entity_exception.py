from .exception import BasicException


class UnProcessableEntityException(BasicException):

    def __init__(self, message):
        BasicException.__init__(self)
        self.status_code = 422
        self.message = message
