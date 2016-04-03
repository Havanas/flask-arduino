import datetime as dt
from flask import render_template
import platform
from app import app
from readtemp import readtemp

@app.route('/')
@app.route('/index')
def index():
    temp = readtemp('/dev/ttyACM0')
    return render_template('home.html',
                           temperature=temp.temperature,
                           units=temp.units.lower())

"""
@app.route('/historical')
def stat_list():
    stats = models.ServerStats.query.all()
    items = reversed([tables.Item(
        s.timestamp.strftime('%H:%M - %m/%d'),
        '{:.2f}'.format(s.cpu_percent),
        '{:.2f}'.format(s.mem_percent)) for s in stats])
    table = tables.HistoricalTable(items, classes=['table'])
    return render_template(
        'stat_list.html',
        server=platform.node(),
        stats=reversed(stats[-10:]),
        table=table,
    )
"""

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
