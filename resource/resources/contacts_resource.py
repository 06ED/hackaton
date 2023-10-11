from flask import request, jsonify

from db.models.contact_model import ContactModel
from resource.resource import Resource


class ContactsResource(Resource):
    address = "contacts"

    @classmethod
    def get(cls):
        return jsonify([
            {
                "id": contact.id,
                "link": contact.link,
                "image": contact.img_url,
                "name": contact.name
            }
            for contact in cls.DATABASE.session.query(ContactModel).all()
        ])
