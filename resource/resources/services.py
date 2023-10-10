from flask import request, jsonify
from resource.resource import Resource


class Services(Resource):
    address = 'services'