#!/usr/bin/env python3
"""A flask application.
"""
from datetime import (
    datetime,
    timezone as tmzn
)
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
import locale
import pytz.exceptions
from typing import Dict, Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    A config for the flask app
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """
    Returns a user dictionary or None if ID value can't be found
    or if 'login_as' URL parameter was not found
    """
    id = request.args.get("login_as", None)
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """Add user to flask.g if user is found
    """
    user = get_user()
    g.user = user
    time_now = pytz.utc.localize(datetime.utcnow())
    time = time_now.astimezone(timezone(get_timezone()))
    locale.setlocale(locale.LC_TIME, (get_locale(), 'UTF-8'))
    fmt = "%b %d, %Y %I:%M:%S %p"
    g.time = time.strftime(fmt)


@babel.localeselector
def get_locale() -> str:
    """Selects and returns the best match of lang from the supported languages
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc

    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    loc = request.headers.get('locale', '')
    if loc in app.config['LANGUAGES']:
        return loc

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """selects and returns custom or default timezone
    """
    tz = request.args.get('timezone')
    try:
        return timezone(tz).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    if g.user:
        try:
            tz = g.user.get('timezone')
            return timezone(tz).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    def_tz = app.config['BABEL_DEFAULT_TIMEZONE']
    return def_tz


@app.route('/', strict_slashes=False)
def index() -> str:
    """Handles the / route
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0", debug=True)
