from flask import request, jsonify
import datetime as dt
from db.models.booking_model import BookingModel
from resource.resource import Resource


class DeleteBookingResource(Resource):
    address = 'services/delete_booking'

    @classmethod
    def post(cls):
        uid = request.json["id"]

        cls.DATABASE.session.delete(BookingModel).filter(BookingModel.id == uid)
        cls.DATABASE.session.commit()