#!/usr/bin/env python3
"""module for task 0"""
from flask import Flask, render_template


app = Flask(__name__)
app.debug = True


@app.route('/', strict_slashes=False)
def index():
    """view function for home page
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
