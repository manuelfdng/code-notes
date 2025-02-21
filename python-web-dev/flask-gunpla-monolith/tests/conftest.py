# tests/conftest.py
import os
import sys
import pytest
from flask import Flask

# Add the parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models.gunpla import Gunpla

@pytest.fixture
def app():
    """Create and configure a test Flask application instance."""
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'WTF_CSRF_ENABLED': False  # Disable CSRF for testing
    })
    
    # Create application context
    with app.app_context():
        # Create all database tables
        db.create_all()
        yield app
        # Clean up
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create a test CLI runner."""
    return app.test_cli_runner()

@pytest.fixture
def sample_gunpla(app):
    """Create a sample Gunpla instance."""
    gunpla = Gunpla(
        name='RX-78-2',
        series='Mobile Suit Gundam',
        grade='MG',
        scale='1/100'
    )
    db.session.add(gunpla)
    db.session.commit()
    return gunpla