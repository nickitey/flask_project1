from flask import Flask, render_template

from data import background, departures, description, subtitle, title, tours

app = Flask(__name__)


@app.route("/departures/<direction>")
def render_departure(direction):
    directions = {}
    for tour in tours:
        if tours[tour]["departure"] == direction:
            directions[tour] = tours[tour]
    return render_template(
        "departure.html",
        departure=departures[direction],
        tours=tours,
        directions=directions,
        departures=departures,
        title=title,
    )


@app.route("/")
def render_index():
    return render_template(
        "index.html",
        description=description,
        departures=departures,
        tours=tours,
        title=title,
        background=background,
        subtitle=subtitle,
    )


@app.route("/tours/<tour>")
def render_tour(tour):
    tour_key = int(tour)
    return render_template(
        "tour.html", tour=tours[tour_key], departures=departures, title=title
    )


@app.errorhandler(500)
def render_server_error(error):
    return f"Что-то не так, но мы все починим, честное слово.", error


@app.errorhandler(404)
def render_404_error(error):
    return render_template(
        "404.html", background=background, departures=departures, title=title
    )


if __name__ == '__main__':
    app.run()

