
from flask import request, jsonify  # pragma: no cover

from connector_db.mongo_db import insert_document
from app import app  # pragma: no cover


"""
This module contains the views and is being ignore in unit tests due to the fact it is already being tested via postman
scripts. This decision may be reviewed in the future and more unit tests specific to this view may be added.
"""


@app.route('/echo', methods=['POST'])  # pragma: no cover
def echo():  # pragma: no cover
    """Simple echo service."""
    message = request.get_json().get('message', '')
    insert_document(message)

    return jsonify({'message': message})
