#!/usr/bin/env python3
"""
A simple Flask app.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Config for the flask app.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Select and return best langguages match based on supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def index() -> str:
    """
    Handles the '/' route
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(port="5001", host="0.0.0.0", debug=True)
