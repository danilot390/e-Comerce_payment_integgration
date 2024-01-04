import os
class Config:
    #Secret key for session managemnt and CSRF protection
    SECRET_KEY = '<SECRET KEY>'

    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:////:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Debug mode
    DEBUG = False