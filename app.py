from flask_cors import CORS

import generator
from config import settings

from flask import Flask
from flask_restful import Api
from db import Database
from misc.utils import Mailer

from resource import register

db = Database(settings.DATABASE_NAME)
app = Flask(__name__)
api = Api(app)
mailer = Mailer(app)
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)


def main():
    generator.generate(db)
    register(api)
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
