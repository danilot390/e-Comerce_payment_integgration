# Configuration for ./config
class InstanceConfig:
    #Secret key for session managemnt and CSRF protection
    SECRET_KEY = 'YOUR SECRET KEY'

    # Database configuration
    SQLALCHEMY_DATABASE_URI = '<DB>://<USER>:<PASWORD>@<PORT>/<DATABASE>'