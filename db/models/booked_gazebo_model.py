import sqlalchemy as sql
from db.main import BaseModel


class BookedGazeboModel(BaseModel):
    email = sql.Column(sql.String, unique=True, nullable=False)
    start_date = sql.Column(sql.DateTime, unique=True, nullable=False)
    end_date = sql.Column(sql.DateTime, unique=True, nullable=False)
