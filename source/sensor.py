from flask import Blueprint, request, Response


from uuid import uuid4


from cache import client


from datetime import datetime


sensor = Blueprint('sensor', __name__)

STATUS = {
    'no_content': ('No content, check the request body', 204),
    'unprocessable_entity': ('Unprocessable entity, check the request attributes', 422)
}


def missing_attributes(document, attributes):
    for attribute in attributes:
        if attribute not in document:
            return True

    return False


def webhook():
    document = request.get_json(force=True, silent=False, cache=False)

    if not document:
        return Response(*STATUS.get('no_content'))

    attributes = ['url']

    if missing_attributes(document, attributes):
        return Response(*STATUS.get('unprocessable_entity'))

    trace = uuid4().hex

    client.publish(
        'webhook',
        str({
            'url': document.get('url'),
            'trace': trace,
            'register': datetime.today().strftime('%x %X'),
            'seconds': document.get('seconds', 5)
        })
    )
    
    return Response(f'Registered {trace}', 200)


sensor.add_url_rule('/webhook', view_func=webhook, methods=['POST'])
