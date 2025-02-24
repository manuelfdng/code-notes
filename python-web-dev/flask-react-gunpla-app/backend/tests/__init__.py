import os
import sys
import pytest

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.models import db
from app.models.gunpla import Gunpla
from config.settings import TestingConfig

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app(TestingConfig)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    yield app
    
    # Clean up / reset resources
    with app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def sample_gunpla(app):
    """Create a sample Gunpla entry."""
    gunpla = Gunpla(
        name="RX-78-2 Gundam",
        series="Mobile Suit Gundam",
        grade="Master Grade",
        scale="1/100"
    )
    with app.app_context():
        db.session.add(gunpla)
        db.session.commit()
        return gunpla

def test_get_gunplas_empty(client):
    """Test getting gunplas when database is empty."""
    response = client.get('/gunplas')
    assert response.status_code == 200
    assert response.json == []

def test_get_gunplas(client, sample_gunpla):
    """Test getting list of gunplas."""
    response = client.get('/gunplas')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['name'] == "RX-78-2 Gundam"
    assert response.json[0]['series'] == "Mobile Suit Gundam"
    assert response.json[0]['grade'] == "Master Grade"
    assert response.json[0]['scale'] == "1/100"

def test_create_gunpla(client):
    """Test creating a new gunpla."""
    data = {
        'name': 'Wing Gundam Zero',
        'series': 'Gundam Wing',
        'grade': 'Perfect Grade',
        'scale': '1/60'
    }
    response = client.post('/gunplas', json=data)
    assert response.status_code == 201
    assert response.json['name'] == data['name']
    assert response.json['series'] == data['series']
    assert response.json['grade'] == data['grade']
    assert response.json['scale'] == data['scale']

def test_create_gunpla_missing_required_fields(client):
    """Test creating a gunpla with missing required fields."""
    data = {
        'name': 'Wing Gundam Zero',
        # Missing series and grade
        'scale': '1/60'
    }
    response = client.post('/gunplas', json=data)
    assert response.status_code == 400
    assert 'Series field is required' in response.json['message']
    assert 'Grade field is required' in response.json['message']

def test_get_gunpla(client, sample_gunpla):
    """Test getting a specific gunpla."""
    response = client.get(f'/gunplas/{sample_gunpla.id}')
    assert response.status_code == 200
    assert response.json['name'] == sample_gunpla.name
    assert response.json['series'] == sample_gunpla.series
    assert response.json['grade'] == sample_gunpla.grade
    assert response.json['scale'] == sample_gunpla.scale

def test_get_nonexistent_gunpla(client):
    """Test getting a gunpla that doesn't exist."""
    response = client.get('/gunplas/999')
    assert response.status_code == 404
    assert response.json['message'] == 'Gunpla model not found'

def test_update_gunpla(client, sample_gunpla):
    """Test updating a gunpla."""
    data = {
        'name': 'Updated Gundam',
        'series': 'Updated Series',
        'grade': 'Updated Grade',
        'scale': '1/144'
    }
    response = client.put(f'/gunplas/{sample_gunpla.id}', json=data)
    assert response.status_code == 200
    assert response.json['name'] == data['name']
    assert response.json['series'] == data['series']
    assert response.json['grade'] == data['grade']
    assert response.json['scale'] == data['scale']

def test_update_nonexistent_gunpla(client):
    """Test updating a gunpla that doesn't exist."""
    data = {
        'name': 'Updated Gundam',
        'series': 'Updated Series',
        'grade': 'Updated Grade',
        'scale': '1/144'
    }
    response = client.put('/gunplas/999', json=data)
    assert response.status_code == 404
    assert response.json['message'] == 'Gunpla model not found'

def test_delete_gunpla(client, sample_gunpla):
    """Test deleting a gunpla."""
    response = client.delete(f'/gunplas/{sample_gunpla.id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Gunpla model deleted successfully'
    
    # Verify gunpla was deleted
    response = client.get(f'/gunplas/{sample_gunpla.id}')
    assert response.status_code == 404

def test_delete_nonexistent_gunpla(client):
    """Test deleting a gunpla that doesn't exist."""
    response = client.delete('/gunplas/999')
    assert response.status_code == 404
    assert response.json['message'] == 'Gunpla model not found'