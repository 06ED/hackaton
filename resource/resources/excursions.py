from flask import request, jsonify
from resource.resource import Resource


class Excursions(Resource):
    address = 'services/excursions'