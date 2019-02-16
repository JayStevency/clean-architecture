from .exception import BasicException


class PaymentRequiredException(BasicException):

    def __init__(self, message):
        BasicException.__init__(self)
        self.status_code = 402
        self.message = message
