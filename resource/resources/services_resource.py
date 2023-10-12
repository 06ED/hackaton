from flask import jsonify

from db.models.service_model import ServiceModel
from resource.resource import Resource


class ServiceResource(Resource):
    address = "service"

    @classmethod
    def get(cls):
        return jsonify([
            {
                "id": service.id,
                "image": service.img_url,
                "name": service.type,
                "description": service.description
            }
            for service in cls.DATABASE.session.query(ServiceModel).all()
        ])
