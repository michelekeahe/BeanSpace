from flask import Blueprint, render_template, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
   data = request.form # Form attribute of request
   return render_template('login.html')

@auth.route('/logout')
def logout():
   return 'logging out!'

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
   if request.method == 'POST':
      name = request.form.get('name')
      username = request.form.get('username')
      email = request.form.get('email')
      password = request.form.get('password')
      confirmPass = request.form.get('confirmPass')

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
         flash("Account created succesffully!")

   return render_template('signup.html')