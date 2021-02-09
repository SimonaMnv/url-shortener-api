from flask import Blueprint, jsonify, request
from shorty.services.base import Services
from shorty.services import error_handler

api = Blueprint('api', __name__)


@api.route('/shortlinks', methods=['POST'])
def create_shortlink():
    data = request.get_json()

    if not data:
        return error_handler.data_not_found()
    if 'url' not in data:
        return error_handler.url_not_found()

    to_shorten = Services(data)

    if to_shorten.wrong_url() and to_shorten.wrong_provider():
        return error_handler.url_provider_invalid_format()
    if to_shorten.wrong_url():
        return error_handler.url_invalid_format()
    if to_shorten.wrong_provider():
        return error_handler.invalid_provider()

    shortened_link = to_shorten.shortened_link()

    return jsonify(shortened_link), 200
