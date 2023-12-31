import email.message as message
import smtplib

from flask import render_template
from config import settings


class Mailer:
    def __init__(self, app):
        self._app = app
        self._smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        self._smtp_server.starttls()
        self._smtp_server.login(settings.EMAIL, settings.PASSWORD)

    def send_success_booking(self, email: str, name, surname, home, start_date, end_date):
        with self._app.app_context():
            msg = message.Message()
            msg["Subject"] = "Ваша заявка на бронирование зарегестрирована!"
            msg.add_header("Content-Type", "text/html")
            msg.set_payload(render_template(
                "success_booking.html",
                name=name,
                surname=surname,
                home=home,
                start_date=start_date.strftime("%m/%d/%Y %H:%M"),
                end_date=end_date.strftime("%m/%d/%Y %H:%M"),
            ))
            self._smtp_server.sendmail(settings.EMAIL, email, msg.as_string().encode("utf-8"))

    def send_success_booking_excursion(self, email: str, name, surname, date, description):
        with self._app.app_context():
            msg = message.Message()
            msg["Subject"] = "Ваша заявка на экскурсию зарегестрирована!"
            msg.add_header("Content-Type", "text/html")
            msg.set_payload(render_template(
                "success_booking_excursion.html",
                name=name,
                surname=surname,
                date=date.strftime("%m/%d/%Y"),
                description=description,
            ))
            self._smtp_server.sendmail(settings.EMAIL, email, msg.as_string().encode("utf-8"))
