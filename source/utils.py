STATUS = {
    'no_content': ('No content, check the request body', 204),
    'unprocessable_entity': ('Unprocessable entity, check the request attributes', 422)
}


def missing_attributes(document, attributes):
    for attribute in attributes:
        if attribute not in document:
            return True

    return False
