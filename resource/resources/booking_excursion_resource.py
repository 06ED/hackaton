import random, string
from flask import request, jsonify
import datetime as dt

from app import mailer
from db.models.booking_excursion_model import BookingExcursionModel
from db.models.booking_model import BookingModel
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
        mailer.send_success_booking_excursion(email, name, surname, date, description)
