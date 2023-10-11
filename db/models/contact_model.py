import sqlalchemy as sql

from db.main import BaseModel


class ContactModel(BaseModel):
    __tablename__ = "contacts"

    img_url = sql.Column(sql.String, unique=True, nullable=True)
    link = sql.Column(sql.String, unique=True, nullable=False)
