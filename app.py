import generator
from config import settings
import datetime as dt

from flask import Flask
from flask_restful import Api
from db import Database
from db.models.booking_house_model import BookingHouseModel
from db.models.booking_pavilion_model import BookingPavilionModel
from db.models.service_model import ServiceModel
from misc.utils import Mailer

from resource import register

db = Database(settings.DATABASE_NAME)
app = Flask(__name__)
api = Api(app)
db = Database(settings.DATABASE_NAME)
mailer = Mailer(app)


def main():
    generator.generate(db)
    register(api)

    renti = BookingPavilionModel(name='awdad', surname='wawadadd', email='dawdawdad', start_date=dt.date(2023, 10, 17), end_date=dt.date(2023, 10, 23), type=2)
    db.session.add(renti)
    db.session.commit()
    app.run()


if __name__ == "__main__":
    main()
