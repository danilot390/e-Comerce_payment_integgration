import pytest
import sys

sys.path.append('/project')

from app import create_app
from app.models import db

# Create aplication
@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })

    with app.app_context():
        db.create_all()

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()