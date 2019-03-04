from unittest import mock

from clean_architecture.domain import InvalidRequestObject
from clean_architecture.domain import UseCase


def test_use_case_cannot_process_valid_requests():
    valid_request_object = mock.MagicMock()
    valid_request_object.__bool__.return_value = True

    use_case = UseCase()
    response = use_case.execute(valid_request_object)

    assert not response
    assert response.type == 500
    assert response.message == \
        "NotImplementedError: process_request() not implemented by UseCase class"  # nopep8


def test_use_case_can_process_invalid_requests_and_returns_response_failure():
    invalid_reuqest_object = InvalidRequestObject()
    invalid_reuqest_object.add_error('someparam', 'somemessage')

    use_case = UseCase()
    response = use_case.execute(invalid_reuqest_object)

    assert not response
    assert response.type == 400
    assert response.message == 'someparam: somemessage'


def test_use_case_can_manage_generic_exception_from_process_request():
    use_case = UseCase()

    class TestException(Exception):
        pass

    use_case.process_request = mock.Mock()
    use_case.process_request.side_effect = TestException('somemessage')
    response = use_case.execute(mock.Mock)

    assert not response
    assert response.type == 500
    assert response.message == 'TestException: somemessage'
