from flask import request
import datetime as dt

from db.models.booking_excursion_model import BookingExcursionModel
from resource.resource import Resource


class BookingResource(Resource):
    address = 'services/booking_excursion'

    @classmethod
    def post(cls):
        name = request.json["name"]
        surname = request.json["surname"]
        email = request.json["email"]
        date = dt.date(request.json["date"])
        description = request.json["description"]

        cls.DATABASE.session.add(BookingExcursionModel(
            name=name,
            surname=surname,
            email=email,
            date=date,
            description=description
        ))
        cls.DATABASE.session.commit()

        from app import mailer
        mailer.send_success_booking_excursion(email, name, surname, date, description)
