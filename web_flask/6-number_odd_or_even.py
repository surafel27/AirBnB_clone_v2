#!/usr/bin/python3
""" flask web application routes to 0.0.0.0:5000/number_template/<int: num>
    render HTML if n is int only and checks if n is even or odd
"""
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


@app.route('/python/')
@app.route('/python/<string:text>')
def pythonIS(text='is cool'):
    """return python <text>"""
    text = text.replace('_', ' ')
    return 'Python %s' % escape(text)


@app.route('/number/<int:n>')
def isNumber(n):
    """return if only n is int"""
    if type(n) == int:
        return "%d is a number" % n


@app.route('/number_template/<int:n>')
def render_number(n):
    """render HTML if n is int"""
    from flask import render_template
    if type(n) == int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def even_odd(n):
    """render HTML if n is int and check for even or odd"""
    from flask import render_template
    if type(n) == int:
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
