from app import db
from base import Base

class User(Base):
    
    name = db.Column(db.String(120), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name