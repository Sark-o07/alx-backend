#!/usr/bin/python3
"""
Setting up a basic flask app.
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles / route
    """

    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(port="5001", host="0.0.0.0", debug=True)