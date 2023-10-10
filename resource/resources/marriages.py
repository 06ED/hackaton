from flask import request, jsonify
from resource.resource import Resource


class Marriages(Resource):
    address = 'services/marriages'