from app import db
from flask import request, jsonify

from db.models.location_model import LocationModel
from resource.resource import Resource


class Dairy(Resource):
    address = 'dairy'

    @staticmethod
    def get():
        locations = db.session.query(LocationModel).all()
        return jsonify({
            "locations": {
                loc.name: [loc.lat, loc.lon] for loc in locations
            }
        })
