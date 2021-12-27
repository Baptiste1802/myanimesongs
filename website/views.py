from flask.app import Flask
from wtforms.fields.simple import HiddenField
from .app import app
from flask import render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from website.models import get_anime, get_animes, get_song, get_songs, get_songs_anime

@app.route("/")
def home():
    return render_template(
        "index.html",
        title="My Anime Songs",
        animes = get_animes()
    )

@app.route("/test")
def test():
    return render_template(
        "test.html"
    )