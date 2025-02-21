# tests/conftest.py
import pytest
import os
import sys
from app import create_app, db
from app.models.gunpla import Gunpla

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'WTF_CSRF_ENABLED': False  # Disable CSRF during testing
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def init_database(app):
    with app.app_context():
        # Add sample data
        sample_gunpla = Gunpla(
            name='RX-78-2',
            series='Mobile Suit Gundam',
            grade='RG',
            scale='1/144'
        )
        db.session.add(sample_gunpla)
        db.session.commit()
        yield db  # this is where the testing happens
        # Cleanup is handled by app fixture