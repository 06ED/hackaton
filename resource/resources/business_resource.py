from flask import request, jsonify
from resource.resource import Resource


class BusinessResource(Resource):
    address = 'business'
