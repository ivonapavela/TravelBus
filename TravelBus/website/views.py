from flask import Blueprint,render_template, request, redirect, url_for, flash
from .models import Trip
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", boolean = current_user.is_admin, user = current_user)


@views.route('/trip', methods= ['GET', 'POST'])
@login_required
def trip():
    return render_template("trip.html", user = current_user)

@views.route('/enter-trip', methods=['GET', 'POST'])
def enter_trip():
    if current_user.is_admin == True :
        if request.method == 'POST' :
            departure = request.form.get('departure')
            destination = request.form.get('destination')
            date = request.form.get('date')
            time = request.form.get('time')
            price=request.form.get('price')

            new_trip = Trip (departure=departure, destination = destination,date = date,time=time, price = price)
            db.session.add(new_trip)
            db.session.commit()
            flash('Trip created!', category = 'success')

        return render_template("enter_trip.html", user=current_user)

    return render_template("enter_trip.html", user=current_user)
