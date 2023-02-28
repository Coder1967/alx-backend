#!/usr/bin/env python3
"""module for task 4"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config class for flask app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """view function for root route
    Returns:
        html: homepage
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """get best matching language
    """
    language = request.args.get("locale")

    if language in app.config["LANGUAGES"]:
        return language
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
