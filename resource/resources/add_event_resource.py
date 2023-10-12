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
        filename = f"{len(os.listdir('media'))}.png"
        file = open(f"media/{filename}", "wb")
        file.write(base64.b64decode(image))
        file.seek(0)
        file.close()

        cls.DATABASE.session.add(AddEventModel(name=name, description=description, image=image))
        cls.DATABASE.session.commit()
