from flask import request, jsonify
import datetime as dt
from resource.resource import Resource


class GetBookingResource(Resource):
    address = "services/booking-cost"

    @classmethod
    def post(cls):
        uid = request.json["id"]

        start_date = dt.datetime.strptime(request.json["start_date"], "%d/%m/%Y").date()
        end_date = dt.datetime.strptime(request.json["end_date"], "%d/%m/%Y").date()

        res = [start_date, end_date]
        dif = dt.timedelta(days=start_date.day, hours=14) - dt.timedelta(days=end_date.day, hours=12)

        if uid <= 3:
            price = 3300 + 250 * (dif.days - 1)
        else:
            day = start_date.weekday()
            if day <= 4:
                price = 1000 * dif.hours
            else:
                price = 1100 * dif.hours

        return jsonify({
            "price": price,
            "res": res
        })
