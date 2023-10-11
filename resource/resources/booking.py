from flask import request, jsonify
from resource.resource import Resource


class Booking(Resource):
    address = 'services/booking'

    @staticmethod
    def post():
        name = request.json['name']
        surname = request.json['surname']
        email = request.json['email']
        start_date = request.json['end_date']
        end_date = request.json['start_date']
        type = request.json['types']