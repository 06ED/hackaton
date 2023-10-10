import sqlalchemy as sql

from db.main import BaseModel


class BookedModel(BaseModel):
    __tablename__ = "booked_houses"

    email = sql.Column(sql.String, unique=True, nullable=False)
    start_date = sql.Column(sql.Date, unique=True, nullable=False)
    end_date = sql.Column(sql.Date, unique=True, nullable=False)
