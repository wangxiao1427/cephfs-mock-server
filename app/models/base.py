from app import db
from sqlalchemy import Column, String, create_engine


class Base(db.Model):

    id = Column(db.Integer, primary_key=True, autoincrement=True)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Object %r>' % self.id
