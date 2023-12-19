# Import necessary modules and classes
from flask import Flask 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Import database instance and configuration from other modules
from .models import db
from .config import Config

# Create a Flask application factory function
def create_app():

    # Initialize the Flask application
    app = Flask(__name__)
    
    # Configure the database URI and disable modification tracking
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/ecommerce_flask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the SQLAlchemy database extension with the Flask application
    db.init_app(app)
    # Initialize the Flask-Migrate extension for handling database migrations    
    migrate = Migrate(app, db)

    # Load additional configuration from a Config class
    app.config.from_object(Config)


    # Return the configured Flask application
    return app