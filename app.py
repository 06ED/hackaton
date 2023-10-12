import os.path

from flask_cors import CORS

import generator
from config import settings

from flask import Flask, send_from_directory
from flask_restful import Api
from db import Database
from misc.utils import Mailer

from resource import register

db = Database(settings.DATABASE_NAME)
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "media"

api = Api(app)
mailer = Mailer(app)
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)


@app.route("/image/<string:file>/")
def download_media(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


def main():
    if not os.path.isdir(app.config["UPLOAD_FOLDER"]):
        os.mkdir(app.config["UPLOAD_FOLDER"])

    generator.generate(db)
    register(api)
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
