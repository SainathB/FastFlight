from datetime import datetime
from app import app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer , primary_key=True)
    email = db.Column('email', db.String(20))
    username = db.Column('username', db.String(50))
    timestamp = db.Column(db.TIMESTAMP, server_default=db.text('CURRENT_TIMESTAMP'))

    def __init__(self, email, username):
        self.email = email
        self.username = username

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def is_active(self):
        return True

    def get_id(self):
        return unicode(self.id)

class City(db.Model):
    __tablename__ = "city"
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column('name', db.String(20))

    def __init__(self, name):
        self.name = name

class Flight(db.Model):
    __tablename__ = "flight"
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column('name', db.String(20))
    from_city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    to_city_id = db.Column(db.Integer, db.ForeignKey('city.id'))

    def __init__(self, name, from_city_id, to_city_id):
        self.name = name
        self.from_city_id = from_city_id
        self.to_city_id = to_city_id

class Journey(db.Model):
    __tablename__ = "journey"
    id = db.Column(db.Integer , primary_key=True)
    timestamp = db.Column(db.TIMESTAMP, server_default=db.text('CURRENT_TIMESTAMP'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'))

    # def __init__(self, )
