from flask import jsonify


class CustomError(Exception):
    def __init__(self, error_message="", status_code=400, suggested_action=None):
        self.error_message = error_message
        self.status_code = status_code
        self.suggested_action = suggested_action

    def to_jsonified(self):
        return jsonify(self.__dict__)


def data_not_found():
    """The server could not understand the request due to invalid syntax."""
    return CustomError(error_message="JSON body is empty",
                       suggested_action="fill JSON body",
                       status_code=400)


def url_not_found():
    """The server could not understand the request due to invalid syntax."""
    return CustomError(error_message="URL parameter not found",
                       suggested_action="add URL parameter",
                       status_code=400)


def url_provider_invalid_format():
    """The server could not understand the request due to invalid syntax."""
    return CustomError(error_message="Both provider and URL are not valid",
                       suggested_action="valid URL example: https://google.com, valid provider examples: bitly, tinyurl",
                       status_code=400)


def url_invalid_format():
    """The server could not understand the request due to invalid syntax."""
    return CustomError(error_message="URL is not valid",
                       suggested_action="valid example: https://google.com",
                       status_code=400)


def invalid_provider():
    """The server could not understand the request due to invalid syntax."""
    return CustomError(error_message="Provider parameter is not valid",
                       suggested_action="tinyurl or bitly",
                       status_code=400)


def wrong_request_parameters():
    """The server could not understand the request due to invalid syntax."""
    return CustomError(error_message="Wrong request parameters",
                       suggested_action="invalid json request: please provide: url and provider or just url",
                       status_code=400)


def both_services_down():
    """The server is not ready to handle the request."""
    return CustomError(error_message="Both tinyurl and bitly are down",
                       suggested_action="try again later",
                       status_code=503)
