from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(1000))

    def __init__(self, username, email, password, name):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
