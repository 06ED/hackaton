from flask import request, jsonify

from db.models.add_event_model import AddEventModel
from resource.resource import Resource


class AddEventResource(Resource):
    address = "add_event"

    @classmethod
    def get(cls):
        title = request.json["title"]
        image = request.json["image"]
        text = request.json["text"]
        cls.DATABASE.session.add(AddEventModel(title=title, text=text, image=image))
        cls.DATABASE.session.commit()