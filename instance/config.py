
class InstanceConfig:
    #Secret key for session managemnt and CSRF protection
    SECRET_KEY = 'CLASH OF KINGS'

    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:""@localhost/ecommerce_flask'
    DEBUG = True
