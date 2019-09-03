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


@app.route('/states', strict_slashes=False, defaults={'id': 'all'})
@app.route('/states/<id>', strict_slashes=False)
def states(id):
    """Route /states"""
    print("SID:", id)
    state = states = None
    if id == 'all':
        states = list(storage.all(State).values())
        states.sort(key=lambda state: state.name)
    else:
        states = storage.all(State)
        key = "State." + id
        if key in states:
            state = states[key]
        else:
            state = None
        states = None
    print("STATES:", states, "STATE:", state)
    return render_template('9-states.html', states=states, state=state)


if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)
