import email.message as message
import smtplib
from email.mime.image import MIMEImage

from flask import render_template
from config import settings


class Mailer:
    def __init__(self, app):
        self._app = app
        self._smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        self._smtp_server.starttls()
        self._smtp_server.login(settings.EMAIL, settings.PASSWORD)

    def send_success_booking(self, email: str, name, surname):
        with self._app.app_context():
            msg = message.Message()
            msg.add_header("Content-Type", "text/html")
            msg.set_payload(render_template(
                "success_booking.html",
                name=name,
                surname=surname
            ))
            self._smtp_server.sendmail(settings.EMAIL, email, msg.as_string().encode("utf-8"))
