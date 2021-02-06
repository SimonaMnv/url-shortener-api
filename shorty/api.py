from flask import Blueprint, jsonify, request, Response
from shorty.services.base import Services

api = Blueprint('api', __name__)


@api.route('/shortlinks', methods=['POST'])
def create_shortlink():
    data = request.get_json()

    if not data:
        return Response("Empty json body", status=400)
    if 'url' not in data:
        return Response("url parameter not found", status=400)

    shortened_link = Services(data).shortened_link()

    return jsonify({"url": data['url'], "link": shortened_link}), 200
