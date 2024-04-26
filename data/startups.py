import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Startups(SqlAlchemyBase):
    __tablename__ = 'startup'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    budget = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    sphere = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    brief_info = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    detailed_info = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_time = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    person = sqlalchemy.Column(sqlalchemy.String, nullable=True)
