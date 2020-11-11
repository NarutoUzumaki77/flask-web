from sqlalchemy import Column, String, Integer
from app import db


class User(db.Model):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    username = Column(String(30), nullable=False)
    email = Column(String(100), nullable=False)

    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "name": self.name
        }
