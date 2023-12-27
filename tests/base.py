# Flask extensions
from flask_testing import TestCase
# App modules
from app import create_app, db

#Base test class
class BaseTestCase(TestCase):

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/ecommerce_flask'
    TESTING = True
    WTF_CSFR_ENABLED = False
    def create_app(self):
        # Create a Flask App with testing configurations
        app = create_app()
        return app
    
    def setUp(self):
        # Set up the test database before each test
        db.create_all()

    def tearDown(self):
        # Tear down the test database after each test
        # db.session.remove()
        # db.drop_all()
        pass

    