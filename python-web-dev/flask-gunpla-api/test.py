import pytest
from app import create_app
from config import TestingConfig
from models import db


@pytest.fixture
def client():
    app = create_app(TestingConfig)
    client = app.test_client()
    # Ensure the database tables are created for each test
    with app.app_context():
        db.drop_all()
        db.create_all()
    yield client


def test_create_gunpla(client):
    payload = {
        'name': 'RX-78-2 Gundam',
        'series': 'Mobile Suit Gundam',
        'grade': 'High Grade',
        'scale': '1/144'
    }
    response = client.post('/gunplas', json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == payload['name']
    assert 'id' in data


def test_get_all_gunplas(client):
    # Create two gunpla models
    gunplas = [
        {'name': 'RX-78-2 Gundam', 'series': 'Mobile Suit Gundam', 'grade': 'High Grade', 'scale': '1/144'},
        {'name': 'Zaku II', 'series': 'Mobile Suit Gundam', 'grade': 'Master Grade', 'scale': '1/100'}
    ]
    for gunpla in gunplas:
        client.post('/gunplas', json=gunpla)
    
    response = client.get('/gunplas')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2


def test_get_single_gunpla(client):
    payload = {
        'name': 'MS-06 Zaku II',
        'series': 'Mobile Suit Gundam',
        'grade': 'Real Grade',
        'scale': '1/144'
    }
    post_response = client.post('/gunplas', json=payload)
    assert post_response.status_code == 201
    gunpla_id = post_response.get_json()['id']
    
    response = client.get(f'/gunplas/{gunpla_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == gunpla_id


def test_update_gunpla(client):
    payload = {
        'name': 'RX-78-2 Gundam',
        'series': 'Mobile Suit Gundam',
        'grade': 'High Grade',
        'scale': '1/144'
    }
    post_response = client.post('/gunplas', json=payload)
    assert post_response.status_code == 201
    gunpla_id = post_response.get_json()['id']
    
    update_payload = {
        'name': 'RX-78-2 Gundam (Updated)',
        'series': 'Mobile Suit Gundam',
        'grade': 'Master Grade',
        'scale': '1/100'
    }
    response = client.put(f'/gunplas/{gunpla_id}', json=update_payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == update_payload['name']
    assert data['grade'] == update_payload['grade']


def test_delete_gunpla(client):
    payload = {
        'name': 'RX-78-2 Gundam',
        'series': 'Mobile Suit Gundam',
        'grade': 'High Grade',
        'scale': '1/144'
    }
    post_response = client.post('/gunplas', json=payload)
    assert post_response.status_code == 201
    gunpla_id = post_response.get_json()['id']
    
    response = client.delete(f'/gunplas/{gunpla_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Gunpla model deleted successfully'
    
    # Verify that the Gunpla model no longer exists
    response = client.get(f'/gunplas/{gunpla_id}')
    assert response.status_code == 404