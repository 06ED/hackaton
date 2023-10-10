from flask import request, jsonify
from resource.resource import Resource


class Rent(Resource):
    address = 'services/rent'