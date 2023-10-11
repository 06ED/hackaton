from flask import request, jsonify

from db.models.add_event_model import AddEventModel
from resource.resource import Resource


class AddEventResource(Resource):
    address = "add_event"

    @classmethod
    def post(cls):
        name = request.json["name"]
        image = request.json["image"]
        description = request.json["description"]
        cls.DATABASE.session.add(AddEventModel(name=name, description=description, image=image))
        cls.DATABASE.session.commit()