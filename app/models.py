from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# Define the User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)

    # Define a representation for User instances (for debugging purposes)
    def __repr__(self):
        return f'<User {self.username}>'
    
    def set_password(self, password):
        # Hash and set the user's password
        self.password = generate_password_hash(password)

    def check_password(self, password):
        # Check if the provided password matches the stored hash
        return check_password_hash(self.password, password)
    
    def get_id(self):
        # Get user's id
        return str(self.id)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

# Define the Sessions model
class Sessions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    start_time = db.Column(db.DateTime)
    expiration_time = db.Column(db.DateTime)

    # Define a representation for Sessions instances (for debugging purposes)
    def __repr__(self):
        return f"Sessions ( {self.suer_id}, '{self.start_time}')"
