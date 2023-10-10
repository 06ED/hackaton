from flask import request, jsonify
import datetime as dt
from config import settings
from db import Database
from db.models.booking_pavilion_model import BookingPavillionModel
from resource.resource import Resource


class BookingPavilion(Resource):
    address = 'services/booking_pavilion'

    def get(self):
        db = Database(settings.DATABASE_NAME)
        res = [(i.start_date, i.end_date) for i in db.query(BookingPavillionModel)]
        return jsonify(res)

    def post(self):
        name = request.json['name']
        surname = request.json['surname']
        email = request.json['email']
        start_date = request.json['end_date']
        end_date = request.json['start_date']
        type = request.json['types']
        db = Database(settings.DATABASE_NAME)
        model = BookingPavillionModel(name=name, surname=surname, email=email, start_date=dt.datetime(start_date),
                             end_date=dt.datetime(end_date), type=type)
        db.session.add(model)
        db.session.commit()
