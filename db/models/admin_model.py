import sqlalchemy as sql

from db.main import BaseModel


class AdminModel(BaseModel):
    __tablename__ = "admins"

    email = sql.Column(sql.String, unique=True, nullable=False)
    is_super_admin = sql.Column(sql.Boolean, default=False)
