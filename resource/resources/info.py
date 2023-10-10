from flask import request, jsonify
from resource.resource import Resource


class Info(Resource):
    address = 'info'
