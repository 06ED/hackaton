from flask import request, jsonify
import datetime as dt
from config import settings
from db import Database
from db.models.booking_pavilion_model import BookingPavilionModel
from resource.resource import Resource


class BookingPavilion(Resource):
    address = 'services/booking_pavilion'

    @classmethod
    def get(cls):
        res = [(i.start_date, i.end_date) for i in cls.DATABASE.query(BookingPavilionModel)]
        return jsonify(res)

    @classmethod
    def post(cls):
        name = request.json['name']
        surname = request.json['surname']
        email = request.json['email']
        start_date = request.json['end_date']
        end_date = request.json['start_date']
        types = request.json['types']

        cls.DATABASE.session.add(BookingPavilionModel(
            name=name,
            surname=surname,
            email=email,
            start_date=dt.datetime(start_date),
            end_date=dt.datetime(end_date),
            type=types
        ))
        cls.DATABASE.session.commit()
