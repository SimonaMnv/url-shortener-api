from flask import Blueprint, jsonify, request, url_for
from shorty.services.base import Services
from shorty.services import error_handler
from shorty.services.error_handler import CustomError

api = Blueprint('api', __name__)


@api.route('/shortlinks', methods=['POST'])
def create_shortlink():
    data = request.get_json()

    if not data:
        raise error_handler.data_not_found()
    if 'url' not in data:
        raise error_handler.url_not_found()

    to_shorten = Services(data)
    to_shorten.check_errors()
    shortened_link = to_shorten.shortened_link()

    return jsonify(shortened_link), 200


@api.errorhandler(CustomError)
def handle_bad_request(error):
    return error.to_jsonified(), error.status_code
