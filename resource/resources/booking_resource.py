import random, string
from flask import request
import datetime as dt

from db.models.booking_model import BookingModel
from resource.resource import Resource


class BookingResource(Resource):
    address = "services/booking"

    @classmethod
    def post(cls):
        name = request.json["name"]
        surname = request.json["surname"]
        email = request.json["email"]
        start_date = dt.datetime.strptime(request.json["end_date"], "%d/%m/%Y").replace(hour=14)
        end_date = dt.datetime.strptime(request.json["start_date"], "%d/%m/%Y").replace(hour=12)
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

        from app import mailer
        mailer.send_success_booking(email, name, surname, types, start_date, end_date)
