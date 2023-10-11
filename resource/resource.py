from typing import Final

import flask_restful

from config import settings
from db import Database


class Resource(flask_restful.Resource):
    DATABASE: Final = Database(settings.DATABASE_NAME)

    address: str
