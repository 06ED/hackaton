import sqlalchemy as sql
from db.main import BaseModel


class ServiceModel(BaseModel):
    __tablename__ = "services"

    type = sql.Column(sql.String, unique=True, nullable=False)
