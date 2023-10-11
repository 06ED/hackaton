import sqlalchemy as sql
from sqlalchemy import orm

from db.main import BaseModel


class AddEventModel(BaseModel):
    __tablename__ = "bookings_ids"

    title = sql.Column(sql.String, unique=False, nullable=False)
    image = sql.Column(sql.String)
    text = sql.Column(sql.String, unique=True, nullable=False)
