# URLs defined & organized in Blueprint/views

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Sprout
from . import db 
import json

views = Blueprint('views', __name__)

#Root route
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
   if request.method == 'POST':
      sprout = request.form.get('sprout')

      # Can only post if meets requirements
      if len(sprout) < 1:
         flash('Sprout is too short!', category='error')
      else:
         new_sprout = Sprout(data=sprout, user_id=current_user.id)
         db.session.add(new_sprout)
         db.session.commit()
         flash('Sprout added!', category='info')
   return render_template('home.html', user=current_user)

@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
   if request.method == 'POST':
      sprout = request.form.get('sprout')

      # Can only post if meets requirements
      if len(sprout) < 1:
         flash('Sprout is too short!', category='error')
      else:
         new_sprout = Sprout(data=sprout, user_id=current_user.id)
         db.session.add(new_sprout)
         db.session.commit()
         flash('Sprout added!', category='info')
   return render_template('profile.html', user=current_user)

@views.route('/delete-sprout', methods=['POST'])
def delete_sprout():
   sprout = json.loads(request.data)
   sproutId = sprout['sproutId']
   sprout = Sprout.query.get(sproutId)
   if sprout:
      if sprout.user_id == current_user.id:
         db.session.delete(sprout)
         db.session.commit()
   return jsonify({})

@views.route('/profile', methods=['GET', 'POST'])
def your_garden():
   return render_template('profile.html', user=current_user)
