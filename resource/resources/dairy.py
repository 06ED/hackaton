from flask import request, jsonify
from resource.resource import Resource


class Dairy(Resource):
    address = 'dairy'