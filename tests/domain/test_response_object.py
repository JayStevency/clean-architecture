import pytest

from clean_architecture.domain import ValidRequestObject, InvalidRequestObject
from clean_architecture.domain import ResponseFailure, ResponseSuccess


@pytest.fixture
def response_value():
    return {'key': ['value1', 'value2']}


@pytest.fixture
def response_type():
    return 'ResponseError'


@pytest.fixture
def response_message():
    return 'This is a response exception'


def test_response_success_is_true(response_value):
    assert bool(ResponseSuccess(200, response_value)) is True


def test_response_failure_is_false(response_type, response_message):
    assert bool(ResponseFailure(response_type, response_message)) is False


def test_response_success_contains_value(response_value):
    response = ResponseSuccess(200, response_value)

    assert response.type == 200
    assert response.value == response_value


def test_response_failure_has_type_and_message(response_type,
                                               response_message):
    response = ResponseFailure(response_type, response_message)

    assert response.type == response_type
    assert response.message == response_message


def test_response_failure_contains_value(response_type, response_message):
    response = ResponseFailure(response_type, response_message)

    assert response.value == {
        'type': response_type, 'message': response_message}


def test_response_failure_initialization_with_exception(response_type):
    response = ResponseFailure(
        response_type, Exception('Just an exception message'))

    assert bool(response) is False
    assert response.type == response_type
    assert response.message == 'Exception: Just an exception message'


def test_response_failure_from_invalid_request_object():
    response = ResponseFailure.build_from_invalid_request_object(
        InvalidRequestObject())

    assert bool(response) is False


def test_response_failure_from_invalid_request_object_with_errors():
    request_object = InvalidRequestObject()
    request_object.add_error('path', 'Is mandatory')
    request_object.add_error('path', "can't be blank")

    response = ResponseFailure.build_from_invalid_request_object(
        request_object)

    assert bool(response) is False
    assert response.type == 400
    assert response.message == "path: Is mandatory\npath: can't be blank"


def test_response_failure_build_resource_error():
    response = ResponseFailure.build_resource_error(message="test message")

    assert bool(response) is False
    assert response.type == 404
    assert response.message == "test message"


def test_response_failure_build_parameters_error():
    response = ResponseFailure.build_parameters_error(message="test message")

    assert bool(response) is False
    assert response.type == 400
    assert response.message == "test message"


def test_response_failure_build_system_error():
    response = ResponseFailure.build_system_error(message="test message")

    assert bool(response) is False
    assert response.type == 500
    assert response.message == "test message"
