from flask import jsonify

from db.models.add_event_model import AddEventModel
from resource.resource import Resource


class EventsResource(Resource):
    address = "events"

    @classmethod
    def get(cls):
        return jsonify([
            {
                "id": event.id,
                "description": event.description,
                "image": event.image,
                "name": event.name
            }
            for event in cls.DATABASE.session.query(AddEventModel).all()
        ])
