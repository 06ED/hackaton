from flask import request, jsonify
from resource.resource import Resource


class Events(Resource):
    address = 'events'