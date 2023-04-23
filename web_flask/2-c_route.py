#!/usr/bin/python3
""" flask web application routes to 0.0.0.0:5000/c/<argument>"""
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNH"""
    return "Hello HBNB!"


@app.route('/hbnb/', strict_slashes=False)
def hbnb():
    """return HBNB on 0.0.0.0:5000/hbnb"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def cisfun(text):
    """print the <text> variable"""
    text = text.replace('_', ' ')
    return "C %s" % escape(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
