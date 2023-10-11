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
        param = {}
        id = request.json["id"]
        pavilion = cls.DATABASE.query(BookingPavilionModel).filter(BookingPavilionModel.id == id).first()
        res = [pavilion.start_date, pavilion.end_date]
        param['res'] = res
        dif = dt.timedelta(res[0]) - dt.timedelta(res[1])
        if id <= 3:
            price = 3300 + 250 * dif.days - 1
        else:
            day = pavilion.start_date.weekday()
            if day == 4:
                price = 1000 * dif.hours
            else:
                price = 1100 * dif.hours
        param['price'] = price
        return jsonify(param)

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
