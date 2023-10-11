from flask import request, jsonify
from resource.resource import Resource


class EventsResource(Resource):
    address = 'events'
