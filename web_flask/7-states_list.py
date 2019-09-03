#!/usr/bin/python3
"""Minimal flask app"""

from flask import Flask, render_template
from models import storage
from models import State
app = Flask(__name__)


@app.teardown_appcontext
def closedb(foo):
    """Closes db session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Route /states_list"""
    print(storage.all(State))
    return render_template('7-states_list.html',
                           states=storage.all(State).values())


if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)
