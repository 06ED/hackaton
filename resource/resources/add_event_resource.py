from flask import request, jsonify

from db.models.add_event_model import AddEventModel
from resource.resource import Resource


class AddEventResource(Resource):
    address = "add_event"

    @classmethod
    def post(cls):
        name = request.json["name"]
        image = request.json["image"]
        decscription = request.json["decscription"]
        cls.DATABASE.session.add(AddEventModel(name=name, decscription=decscription, image=image))
        cls.DATABASE.session.commit()