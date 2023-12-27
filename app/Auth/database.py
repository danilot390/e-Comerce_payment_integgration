from app.models import db, User

def create_user(username, email, password):
    # Create a new user and add to the database
    new_user = User (username=username, email=email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

def get_user_by_username(username):
    # Retrieve a user by username
    return User.query.filter_by(username=username).first()

def get_user_by_email(email):
    # Retrieve a user by email
    return User.query.filter_by(email=email).first()