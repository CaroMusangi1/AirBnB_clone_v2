#!/usr/bin/bash
"""
Starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def app_teardown(arg=None):
    """close the current session """
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    """
    Displays an HTML page with a list of all State objects in DBStorage
    and its cities.States are sorted by name.
    """
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
