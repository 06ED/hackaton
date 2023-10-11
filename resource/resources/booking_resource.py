import random, string
from flask import request, jsonify
import datetime as dt

from app import mailer
from db.models.booking_model import BookingModel
from resource.resource import Resource


class BookingResource(Resource):
    address = 'services/booking'

    @classmethod
    def get(cls):
        uid = request.json["id"]
        booking = cls.DATABASE.query(BookingModel).filter(BookingModel.id == uid).first()
        res = [booking.start_date, booking.end_date]
        dif = dt.timedelta(res[0]) - dt.timedelta(res[1])

        if uid <= 3:
            price = 3300 + 250 * (dif.days - 1)
        else:
            day = booking.start_date.weekday()
            if day <= 4:
                price = 1000 * dif.hours
            else:
                price = 1100 * dif.hours

        return jsonify({
            "price": price,
            "res": res
        })

    @classmethod
    def post(cls):
        name = request.json["name"]
        surname = request.json["surname"]
        email = request.json["email"]
        start_date = dt.datetime(request.json["end_date"], hour=14)
        end_date = dt.datetime(request.json["start_date"], hour=12)
        types = request.json["types"]

        cls.DATABASE.session.add(BookingModel(
            name=name,
            surname=surname,
            email=email,
            start_date=start_date,
            end_date=end_date,
            type=types
        ))
        cls.DATABASE.session.add(BookingModel(
            booking_id=cls.DATABASE.query(BookingModel).filter(BookingModel.email == email).first().id,
            uniq_num=''.join(random.choice(string.ascii_lowercase + '0123456789') for i in range(15))
        ))
        cls.DATABASE.session.commit()
        mailer.send_success_booking(email, name, surname, types, start_date, end_date)
