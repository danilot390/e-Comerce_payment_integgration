# Import necessary modules and classes
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Import database instance and configuration from other modules
from .models import db, User
from .config import Config
from .Auth import auth

# Create a Flask application factory function
def create_app():
    # Initialize the Flask application
    app = Flask(__name__)
    
    # Load additional configuration from a Config class
    app.config.from_object(Config)
    
    # Initialize the SQLAlchemy database extension with the Flask application
    db.init_app(app)

    # Initialize the Flask-Migrate extension for handling database migrations    
    migrate = Migrate(app, db)

    

    # Initialize Flask-Login
    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    app.register_blueprint(auth) #Auth Blueprint

    @app.route('/home')
    def home():
        context ={
        }
        return render_template('index.html', **context)

    # Return the configured Flask application
    return app