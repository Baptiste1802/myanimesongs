from flask import Flask
from flask_bootstrap5 import Bootstrap
from flask_sqlalchemy import SQLAlchemy 
import os.path
from flask_login import LoginManager, login_manager

app = Flask(__name__)
Bootstrap(app)

def mkpath(path):
    return os.path.normpath(
        os.path.join(os.path.dirname(__file__), path)
    )

app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///'+mkpath('database/songs.db')
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.config['SECRET_KEY'] = '328396918c21bf73e52e9b867c7a2dcb88a083e200022e7380bc280e3017a617'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'