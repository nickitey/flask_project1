from flask import Flask, render_template
from data import title, subtitle, description, departures, tours


app = Flask(__name__)


@app.route('/departure')
def render_departure():
    return render_template('departure.html')


@app.route('/')
def render_index():
    return render_template('index.html', description=description,
                           departures=departures, tours=tours, title=title, subtitle=subtitle)


@app.route('/tours/<tour>')
def render_tour(tour):
    tour_key = int(tour)
    return render_template('tour.html', tour=tours[tour_key],
                           departures=departures, title=title)


app.run('0.0.0.0', 8000)
