import sqlalchemy as sql

from db.main import BaseModel


class RentModel(BaseModel):
    __tablename__ = "rents"

    name = sql.Column(sql.String, nullable=False)
    img_url = sql.Column(sql.String)
    description = sql.Column(sql.Text, nullable=True)
    cost = sql.Column(sql.String, nullable=False)