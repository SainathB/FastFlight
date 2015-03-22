from flask import session, request, flash, url_for, redirect, render_template, abort ,g , make_response
from app import app
from datetime import datetime
from models import *
from flask.ext.login import login_user , logout_user , current_user , login_required
from functools import wraps
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic
from config import CONFIG

authomatic = Authomatic(CONFIG, 'abcde', report_errors=False)
@app.route('/', methods=['GET', 'POST'])
def index():
    if g.user.is_authenticated():
        return render_template('search.html')
    else:
        return redirect(url_for('login'))

@app.route('/login')
def login():
	return render_template("login.html")
		
@app.route('/login/google',methods=['GET', 'POST'])
def login_google():
    # We need response object for the WerkzeugAdapter.
    response = make_response()
    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), 'google')
    user = None
    if result:
        if result.user:
            result.user.update()
            user = User.query.filter_by(email=result.user.email).first()
            if user is None:
                user = User(result.user.email,result.user.name)
                db.session.add(user)
                db.session.commit()
        login_user(user, remember = True)
        return redirect(request.args.get('next') or url_for('index'))
    return response

@app.route('/selectflight', methods=['GET','POST'])
def select_flight():
    from_city = City.query.filter_by(name=request.form['city_from']).first()
    to_city = City.query.filter_by(name=request.form['city_to']).first()
    flights = Flight.query.filter_by(from_city_id=from_city.id, to_city_id=to_city.id).all()
    return render_template("select_flight.html", from_city=from_city, to_city=to_city, flights=flights)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login')) 

@app.before_request
def before_request():
    g.user = current_user

