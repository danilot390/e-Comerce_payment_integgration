from flask_sqlalchemy import SQLAlchemy

# Create a SQLAchemy instance
db = SQLAlchemy()

# Imported models 
from .auth import User, Sessions