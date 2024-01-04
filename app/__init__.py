# Import necessary modules and classes
from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager

# Import database instance and configuration from other modules
from .models import db, User
from config import Config
from instance.config import InstanceConfig
from .config import AppConfig
from .apps.auth import auth
from .main import main

# Create a Flask application factory function
def create_app():
    # Initialize the Flask application
    app = Flask(__name__)
    
    # Load configuration from a Config class
    app.config.from_object(Config)
    # Load instance-specific configurations
    app.config.from_object(InstanceConfig)
    # Override Flask app-specific configuration
    app.config.from_object(AppConfig)
    
    # Initialize the SQLAlchemy database extension with the Flask application
    db.init_app(app)

    # Initialize the Flask-Migrate extension for handling database migrations    
    migrate = Migrate(app, db)

    # Initialize Flask-Login
    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'

    # Load User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    app.register_blueprint(auth) # Auth Blueprint
    app.register_blueprint(main) # Main Blueprint

    # Return the configured Flask application
    return app