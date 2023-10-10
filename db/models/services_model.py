import sqlalchemy as sql
from db.main import BaseModel


class Services(BaseModel):
    __tablename__ = 'services'

    type = sql.Column(sql.String, unique=True, nullable=False)
