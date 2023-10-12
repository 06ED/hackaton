import sqlalchemy as sql
from sqlalchemy import orm

from db.main import BaseModel


class BookingExcursionModel(BaseModel):
    __tablename__ = "bookings_excursions"

    name = sql.Column(sql.String, unique=False, nullable=False)
    surname = sql.Column(sql.String, unique=False, nullable=False)
    email = sql.Column(sql.String, unique=True, nullable=False)
    date = sql.Column(sql.Date, unique=False, nullable=False)
    description = sql.Column(sql.String, nullable=False)
