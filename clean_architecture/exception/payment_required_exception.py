from .exception import BasicException


class PaymentRequiredException(BasicException):

    def __init__(self, error_code, message):
        BasicException.__init__(self)
        self.status_code = 402
        self.error_code = error_code
        self.message = message
