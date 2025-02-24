# tests/test_routes.py
import pytest
from flask import url_for
from app.models.gunpla import Gunpla
from app import db

def test_index_route(client):
    """Test the index route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Gunpla Models' in response.data

def test_create_route_get(client):
    """Test accessing the create form."""
    response = client.get('/create')
    assert response.status_code == 200
    assert b'Add New Gunpla' in response.data

def test_create_route_post(client):
    """Test creating a new Gunpla."""
    response = client.post('/create', data={
        'name': 'Strike Freedom',
        'series': 'Gundam SEED Destiny',
        'grade': 'PG',
        'scale': '1/60'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Gunpla model added successfully!' in response.data
    assert b'Strike Freedom' in response.data

def test_edit_route(client, sample_gunpla):
    """Test editing an existing Gunpla."""
    # Get the edit form
    response = client.get(f'/edit/{sample_gunpla.id}')
    assert response.status_code == 200
    assert b'Edit Gunpla' in response.data
    
    # Submit the edit form
    response = client.post(f'/edit/{sample_gunpla.id}', data={
        'name': 'RX-78-2 Ver.Ka',
        'series': 'Mobile Suit Gundam',
        'grade': 'MG',
        'scale': '1/100'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Gunpla model updated successfully!' in response.data
    assert b'RX-78-2 Ver.Ka' in response.data

def test_delete_route(client, sample_gunpla):
    """Test deleting a Gunpla."""
    response = client.post(f'/delete/{sample_gunpla.id}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Gunpla model deleted successfully!' in response.data
    assert sample_gunpla.name.encode() not in response.data

def test_404_route(client):
    """Test accessing a non-existent Gunpla."""
    response = client.get('/edit/999')
    assert response.status_code == 404