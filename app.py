from flask import Flask, render_template

app = Flask(__name__)


@app.route('/departure')
def render_departure():
    return render_template('departure.html')


@app.route('/')
def render_index():
    return render_template('index.html')


@app.route('/tour')
def render_tour():
    return render_template('tour.html')


app.run('0.0.0.0', 8000)
