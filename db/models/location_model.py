import sqlalchemy as sql

from db.main import BaseModel


class LocationModel(BaseModel):
    __tablename__ = "locations"

    name = sql.Column(sql.String)
    lat = sql.Column(sql.Double, nullable=False)
    lon = sql.Column(sql.Double, nullable=False)
