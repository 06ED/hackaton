from flask import request, jsonify
from resource.resource import Resource


class Index(Resource):
    address = ''