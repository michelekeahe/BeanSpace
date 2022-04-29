from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_user, login_required
from werkzeug.security import generate_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

# Login request form-- users cannot login without proper credentials already stored in database
@auth.route('/login', methods=['GET', 'POST'])
def login():
   data = request.form # Form attribute of request
   return render_template('login.html')

# Logout only if a user is already logged in
@auth.route('/logout')
def logout():
   return 'logging out!'

# Sign user up as long as the credentials don't conflict with what's inside database
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
   if request.method == 'POST':
      # get all data inputted
      name = request.form.get('name')
      username = request.form.get('username')
      email = request.form.get('email')
      password = request.form.get('password')
      confirmPass = request.form.get('confirmPass')
      
      # If all fields are filled out correctly, create an account
      if len(name) < 2:
         flash("Name must be greater than 1 character.", category='error')
      elif len(username) < 2:
         flash("username must be greater than 1 character.", category='error')
      elif len(email) < 4:
         flash("email must be greater than 3 characters.", category='error')
      elif password != confirmPass:
         flash("Passwords don\'t match.", category='error')
      elif len(password) < 4:
         flash("Password must be greater than 3 characters.", category='error')
      else:
         # Apply all data into a user query & commit to database
         new_user = User(name=name, username=username, email=email, password=generate_password_hash(password, method='sha256'))
         db.session.add(new_user)
         db.session.commit()
         login_user(new_user, remember=True)
         flash("Account created succesfully!")
         return redirect(url_for('views.home')) # Redirect to home once account is made


   return render_template('signup.html')