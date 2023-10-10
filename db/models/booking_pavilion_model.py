import sqlalchemy as sql
from sqlalchemy import orm

from db.main import BaseModel


class BookingPavillionModel(BaseModel):
    __tablename__ = "booking_pavillion"

    name = sql.Column(sql.String, unique=False, nullable=False)
    surname = sql.Column(sql.String, unique=False, nullable=False)
    email = sql.Column(sql.String, unique=True, nullable=False)
    start_date = sql.Column(sql.DateTime, unique=False, nullable=False)
    end_date = sql.Column(sql.DateTime, unique=False, nullable=False)
    type = sql.Column(sql.Integer, sql.ForeignKey('services.id'), unique=False, nullable=False)

    types = orm.relationship("ServicesModel", backref='booking')
