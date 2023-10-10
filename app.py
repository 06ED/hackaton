from config import settings
import datetime as dt

from flask import Flask
from flask_restful import Api
from db import Database
from db.models.booking_house_model import BookingModel
from db.models.services_model import ServicesModel
from resource import register

app = Flask(__name__)
api = Api(app)
db = Database(settings.DATABASE_NAME)


def main():
    register(api)
    rent1 = ServicesModel(type="Гостевой домик 1")
    rent2 = ServicesModel(type="Гостевой домик 2")
    rent3 = ServicesModel(type="Гостевой домик 3 (ЭКО)")
    rent4 = ServicesModel(type="Беседка на воде")
    rent5 = ServicesModel(type="Беседка у пруда")
    db.session.add(rent1)
    db.session.add(rent2)
    db.session.add(rent3)
    db.session.add(rent4)
    db.session.add(rent5)
    renti = BookingModel(name='awdad', surname='wawadadd', email='dawdawdad', start_date=dt.date(2023, 10, 17), end_date=dt.date(2023, 10, 23), type=2)
    db.session.add(renti)
    db.session.commit()
    app.run()


if __name__ == "__main__":
    main()