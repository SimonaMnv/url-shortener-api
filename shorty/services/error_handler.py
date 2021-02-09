from flask import jsonify


def data_not_found():
    return jsonify(error_message="JSON body is empty",
                   suggested_action="fill JSON body",
                   status_code=400), 400


def url_not_found():
    return jsonify(error_message="URL parameter not found",
                   suggested_action="add URL parameter",
                   status_code=400), 400


def url_provider_invalid_format():
    return jsonify(error_message="Both provider and URL are not valid",
                   suggested_action="valid URL example: https://google.com, valid provider examples: bitly, tinyurl",
                   status_code=400), 400


def url_invalid_format():
    return jsonify(error_message="URL is not valid",
                   suggested_action="valid example: https://google.com",
                   status_code=400), 400


def invalid_provider():
    return jsonify(error_message="Provider parameter is not valid",
                   suggested_action="tinyurl or bitly",
                   status_code=400), 400

