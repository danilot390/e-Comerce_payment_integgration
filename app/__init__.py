from flask import Flask 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Config

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/ecommerce_flask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config.from_object(Config)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    return app