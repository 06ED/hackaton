from flask import request, jsonify
from resource.resource import Resource


class InfoResource(Resource):
    address = 'info'
