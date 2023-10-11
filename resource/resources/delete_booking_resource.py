from flask import request, jsonify
import datetime as dt
from db.models.booking_model import BookingModel
from resource.resource import Resource


class DeleteBookingResource(Resource):
    address = 'services/delete_booking'

    @classmethod
    def get(cls):
        uniq_num = request.json["uniq_num"]

        cls.DATABASE.session.delete(BookingModel).filter(BookingModel.uniq_num == uniq_num)
        cls.DATABASE.session.commit()