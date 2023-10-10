from flask import request, jsonify
from resource.resource import Resource


class Business(Resource):
    address = 'business'