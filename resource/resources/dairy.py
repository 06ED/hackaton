from flask import jsonify

from db.models.location_model import LocationModel
from resource.resource import Resource


class Dairy(Resource):
    address = "dairy"

    @classmethod
    def get(cls):
        locations = cls.DATABASE.session.query(LocationModel).all()
        return jsonify({
            "locations": {
                loc.name: [loc.lat, loc.lon] for loc in locations
            }
        })
