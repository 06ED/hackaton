import os
import base64

from flask import request

from db.models.add_event_model import AddEventModel
from resource.resource import Resource


class AddEventResource(Resource):
    address = "add_event"

    @classmethod
    def post(cls):
        name = request.json["name"]
        image = request.json["image"]
        description = request.json["description"]

        filename = f"{os.listdir('media')}.png"
        with open(f"../media/{filename}", "wb") as file:
            file.write(base64.b64decode(image))

        cls.DATABASE.session.add(AddEventModel(name=name, description=description, image=image))
        cls.DATABASE.session.commit()
