import os
class Config:
    #Secret key for session managemnt and CSRF protection
    SECRET_KEY = 'CLASH OF KINGS'

    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/ecommerce_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Debug mode
    DEBUG = True