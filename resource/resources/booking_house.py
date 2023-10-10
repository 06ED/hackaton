from flask import request, jsonify
import datetime as dt
from config import settings
from db import Database
from db.models.booking_house_model import BookingHouseModel
from resource.resource import Resource


class BookingHouse(Resource):
    address = 'services/booking_house'

    def get(self):
        db = Database(settings.DATABASE_NAME)
        res = [(i.start_date, i.end_date) for i in db.query(BookingHouseModel)]
        return jsonify(res)

    def post(self):
        name = request.json['name']
        surname = request.json['surname']
        email = request.json['email']
        start_date = request.json['end_date']
        end_date = request.json['start_date']
        type = request.json['types']
        db = Database(settings.DATABASE_NAME)
        model = BookingHouseModel(name=name, surname=surname, email=email, start_date=dt.datetime(start_date),
                             end_date=dt.datetime(end_date), type=type)
        db.session.add(model)
        db.session.commit()
