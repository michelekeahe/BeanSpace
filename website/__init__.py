from tabnanny import check
from unicodedata import category
from django.shortcuts import redirect
from flask import Flask, request, flash, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_HOST = 'localHost'
DB_NAME = 'beanDB'
DB_USER = 'postgres'
DB_PASS = 'password'

def create_app():
   app = Flask('__name__')
   app.config['SECRET_KEY'] = 'mysecretkey'
   app.config['SQLALCHEMY_DATABASE_URI'] = f'postgres://postgres:postgres@localhost/{DB_NAME}' # Store in Database
   db.init_app(app) #

   from .views import views
   from .auth import auth

   app.register_blueprint(views, url_prefix='/')
   app.register_blueprint(auth, url_prefix='/')
   return app