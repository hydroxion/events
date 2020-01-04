from flask import Blueprint, request, jsonify


from time import sleep


from random import choice


process = Blueprint('process', __name__)


def status():
    document = request.get_json(force=True, silent=False, cache=False)

    if document.get('sleep') and type(document.get('sleep')) == int and document.get('sleep') > 0:
        sleep(document.get('sleep'))

    return jsonify({'status': choice([True, False])}), 200


process.add_url_rule('/status', view_func=status, methods=['POST'])
