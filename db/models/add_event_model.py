import sqlalchemy as sql
from sqlalchemy import orm

from db.main import BaseModel


class AddEventModel(BaseModel):
    __tablename__ = "bookings_ids"

    image = sql.Column(sql.String)
    text = sql.Column(sql.String, unique=True, nullable=False)
