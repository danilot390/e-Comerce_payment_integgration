from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Define a representation for User instances (for debugging purposes)
    def __repr__(self):
        return f"User( '{self.username}', '{self.email}')"

# Define the Sessions model
class Sessions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    start_time = db.Column(db.DateTime)
    expiration_time = db.Column(db.DateTime)

    # Define a representation for Sessions instances (for debugging purposes)
    def __repr__(self):
        return f"Sessions ( {self.suer_id}, '{self.start_time}')"
