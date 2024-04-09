#!/usr/bin/env python3
"""
Basic flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Config for flask app
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def index() -> str:
    """
    Handles / route
    """

    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(port="5001", host="0.0.0.0", debug=True)
