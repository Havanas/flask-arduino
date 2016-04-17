import datetime as dt
from flask import render_template
import platform
from app import app
from readtemp import readtemp

@app.route('/')
@app.route('/index')
def index():
    temp = readtemp('/dev/ttyACM1')
    return render_template('home.html',
                           temperature=temp.temperature,
                           units=temp.units.lower())


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
