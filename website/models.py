import email
from email.policy import default
from time import timezone
from click import password_option
from . import db # from this website package
from flask_login import UserMixin
from sqlalchemy.sql import func

# Sprout class - posts
class Sprout(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   data  = db.Column(db.String(300))
   date = db.Column(db.DateTime(timezone=True), default=func.now())   
   user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Pass valid ID/primary key of existing ID - one-to-many

# User class (will be lowercase in SQL)
class User(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(150), unique=True) 
   email = db.Column(db.String(150), unique=True)
   password = db.Column(db.String(150))
   name = db.Column(db.String(150))
   sprouts = db.relationship('Sprout')
