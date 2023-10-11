import sqlalchemy as sql
from sqlalchemy import orm

from db.main import BaseModel


class BookingIdModel(BaseModel):
    __tablename__ = "bookings_ids"

    booking_id = sql.Column(sql.Integer, sql.ForeignKey("bookings.id"), unique=False, nullable=False)
    uniq_num = sql.Column(sql.String, unique=True, nullable=False)

    bookings = orm.relationship("BookingModel", backref="bookings_ids")
