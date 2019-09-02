#!/usr/bin/python3
"""Minimal flask app"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False
app.run("0.0.0.0", 5000)


@app.route('/')
def index():
    """Route index"""
    print("Hello HBNB!")
