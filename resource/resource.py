import flask_restful

from config import settings
from db import Database


class Resource(flask_restful.Resource):
    DATABASE = Database(settings.DATABASE_NAME)

    address: str
