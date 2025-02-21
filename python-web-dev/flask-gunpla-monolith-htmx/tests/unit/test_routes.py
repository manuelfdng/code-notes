# tests/unit/test_routes.py
import pytest
from app.models.gunpla import Gunpla
from app import db

def test_index_page(client, init_database):
    """Test the index page loads correctly"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'RX-78-2' in response.data
    assert b'Mobile Suit Gundam' in response.data

def test_create_gunpla(client, init_database):
    """Test creating a new Gunpla entry"""
    response = client.post('/create', data={
        'name': 'Exia',
        'series': 'Gundam 00',
        'grade': 'MG',
        'scale': '1/100'
    })
    assert response.status_code == 302  # Redirect after successful creation
    
    # Check if the new Gunpla was added
    response = client.get('/')
    assert b'Exia' in response.data
    assert b'Gundam 00' in response.data

def test_edit_gunpla(client, init_database, app):
    """Test editing an existing Gunpla entry"""
    with app.app_context():
        response = client.post('/edit/1', data={
            'name': 'RX-78-2 Gundam',
            'series': 'Mobile Suit Gundam',
            'grade': 'PG',
            'scale': '1/60'
        })
        assert response.status_code == 200
        assert b'PG' in response.data
        assert b'1/60' in response.data
        
        # Verify changes in database
        edited_gunpla = db.session.get(Gunpla, 1)
        assert edited_gunpla.grade == 'PG'
        assert edited_gunpla.scale == '1/60'

def test_delete_gunpla(client, init_database, app):
    """Test deleting a Gunpla entry"""
    with app.app_context():
        response = client.post('/delete/1')
        assert response.status_code == 200
        
        # Verify the Gunpla was deleted
        deleted_gunpla = db.session.get(Gunpla, 1)
        assert deleted_gunpla is None

def test_get_edit_form(client, init_database, app):
    """Test retrieving the edit form via HTMX"""
    with app.app_context():
        response = client.get('/gunpla/1/edit-form')
        assert response.status_code == 200
        assert b'form' in response.data
        assert b'RX-78-2' in response.data

def test_get_gunpla_row(client, init_database, app):
    """Test retrieving a single Gunpla row via HTMX"""
    with app.app_context():
        response = client.get('/gunpla/1')
        assert response.status_code == 200
        assert b'RX-78-2' in response.data
        assert b'Mobile Suit Gundam' in response.data

def test_404_handling(client, app):
    """Test handling of non-existent Gunpla IDs"""
    with app.app_context():
        response = client.get('/gunpla/999')
        assert response.status_code == 404