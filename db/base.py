import sqlalchemy as sql

from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
    id = sql.Column(sql.Integer, autoincrement=True, unique=True, primary_key=True)
