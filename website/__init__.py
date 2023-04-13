# __init__.py implicitely executes file & mark directories

from tabnanny import check
from unicodedata import category
from flask import Flask
from flask_login import LoginManager, login_manager
from flask_sqlalchemy import SQLAlchemy
from os import path

# Define database & variables
db = SQLAlchemy()
DB_HOST = 'localHost'
DB_NAME = 'beanDB'
DB_USER = 'postgres'
DB_PASS = 'password'

# Creating web application, registering blueprints & location for database
def create_app():
   app = Flask('__name__') #special variable that gets value depending on how script is executed
   app.config['SECRET_KEY'] = 'mysecretkey' #In production, don't share
   app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:password@localhost/{DB_NAME}' # Store in Database
   db.init_app(app) 

   # import files
   from .views import views
   from .auth import auth

   # Register blueprints & add prefix if want
   app.register_blueprint(views, url_prefix='/')
   app.register_blueprint(auth, url_prefix='/')

   from .models import User, Sprout

   # Use this app with the database
   create_database(app)

   # Where to redirect if not logged in
   login_manager = LoginManager()
   login_manager.login_view = 'auth.login'
   login_manager.init_app(app)

   # Tell flask how to load user
   @login_manager.user_loader
   def load_user(id):
      # similar to filter_by but defaults to primary key instead
      return User.query.get(int(id))

   return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')