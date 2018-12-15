import json

from flask import request, jsonify  # pragma: no cover

from connector_db.mongo_db import insert_document, get_all
from app import app  # pragma: no cover
from utils import get_str_from_date_isoformat

"""
This module contains the views and is being ignore in unit tests due to the fact it is already being tested via postman
scripts. This decision may be reviewed in the future and more unit tests specific to this view may be added.
"""


@app.route('/insert_data', methods=['POST'])  # pragma: no cover
def insert_data():  # pragma: no cover
    """Simple echo service."""
    message = request.get_json().get('data')
    message['date'] = get_str_from_date_isoformat()

    last_insert_id = insert_document(message)

    return jsonify({'insert_object_id': str(last_insert_id)})


@app.route('/get_data', methods=['POST'])  # pragma: no cover
def get_data():  # pragma: no cover
    """Simple echo service."""

    lst = get_all()
    return jsonify({'data': lst})


@app.route('/echo', methods=['POST'])  # pragma: no cover
def echo():  # pragma: no cover
    """Simple echo service."""
    message = request.get_json().get('message', '')

    return jsonify({'message': message})
