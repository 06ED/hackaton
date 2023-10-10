from flask import request

from misc.utils import send_mail
from resource.resource import Resource


class MailResource(Resource):
    address = "email/verify"

    @staticmethod
    def post():
        email = request.json["email"]
        send_mail(email)
