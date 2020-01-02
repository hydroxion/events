from flask import Flask

from state import state

from flask import Blueprint, request, Response

from types import MappingProxyType

from uuid import uuid4


__all__ = ['sensors', 'webhook']


sensors = Blueprint('sensors', __name__)

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

    state.append(
        MappingProxyType({
            'url': document.get('url'),
            'trace': trace,
            'position': len(state)
        })
    )

    return Response(f'Request registered, trace {trace}', 200)


sensors.add_url_rule('/webhook', view_func=webhook, methods=['POST'])