from config import settings

from flask import Flask
from flask_restful import Api
from db import Database
from misc.utils import Mailer

from resource import register

app = Flask(__name__)
api = Api(app)
db = Database(settings.DATABASE_NAME)
mailer = Mailer(app)


def main():
    register(api)
    app.run(debug=True)


if __name__ == "__main__":
    main()
