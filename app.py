from flask import Flask, render_template
from data import title, subtitle, description, departures, tours, background


app = Flask(__name__)


@app.route('/departures/<direction>')
def render_departure(direction):
    directions = {}
    for tour in tours:
        if tours[tour]['departure'] == direction:
            directions[tour] = tours[tour]
    return render_template('departure.html', departure=departures[direction],
                           tours=tours, directions=directions, departures=departures,
                           title=title)


@app.route('/')
def render_index():
    return render_template('index.html', description=description,
                           departures=departures, tours=tours, title=title,
                           background=background, subtitle=subtitle)


@app.route('/tours/<tour>')
def render_tour(tour):
    tour_key = int(tour)
    return render_template('tour.html', tour=tours[tour_key],
                           departures=departures, title=title)


app.run('0.0.0.0', 8000)
