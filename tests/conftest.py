import pytest
import sys

sys.path.append('/project')

import app.create_all
import app.db

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