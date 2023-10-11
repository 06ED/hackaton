import sqlalchemy as sql
from sqlalchemy import orm

from db.main import BaseModel


class AddEventModel(BaseModel):
    __tablename__ = "bookings_ids"

    name = sql.Column(sql.String, unique=False, nullable=False)
    image = sql.Column(sql.String)
    description = sql.Column(sql.String, unique=True, nullable=False)
