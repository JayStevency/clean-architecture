class ResponseSuccess:

    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __nonzero__(self):
        return True

    __bool__ = __nonzero__


class ResponseFailure:

    def __init__(self, type_, error_code, message):
        self.type = type_
        self.error_code = error_code
        self.message = self._format_message(message)

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return "{}: {}".format(msg.__class__.__name__, "{}".format(msg))
        return msg

    @property
    def value(self):
        return {'type': self.type, 'error_code': self.error_code, 'message': self.message}

    def __bool__(self):
        return False

    @classmethod
    def build_resource_error(cls, status_code=404, error_code=None, message=None):
        return cls(status_code, error_code, message)

    @classmethod
    def build_system_error(cls, status_code=500, error_code=None, message=None):
        return cls(status_code, error_code, message)

    @classmethod
    def build_parameters_error(cls, status_code=400, error_code=None, message=None):
        return cls(status_code, error_code, message)

    @classmethod
    def build_from_invalid_request_object(cls, invalid_request_object):
        message = "\n".join(["{}: {}".format(err['parameter'], err['message'])
                             for err in invalid_request_object.errors])
        return cls.build_parameters_error(message=message)
