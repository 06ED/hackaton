from flask import request, jsonify

from db.models.rent_model import RentModel
from resource.resource import Resource


class RentResource(Resource):
    address = "services/rent"

    @classmethod
    def get(cls):
        return jsonify([
            {
                "id": rent.id,
                "name": rent.name,
                "description": rent.description,
                "cost": rent.cost,
                "img_url": rent.img_url
            } for rent in cls.DATABASE.session.query(RentModel).all()
        ])

    @classmethod
    def post(cls):
        uid = request.json["id"]
        rent = cls.DATABASE.session.query(RentModel).filter(RentModel.id == uid).first()
        return jsonify({
            "id": rent.id,
            "name": rent.name,
            "description": rent.description,
            "cost": rent.cost,
            "img_url": rent.img_url
        })

