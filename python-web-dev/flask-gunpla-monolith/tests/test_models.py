# tests/test_models.py
import pytest
from app.models.gunpla import Gunpla
from app import db

def test_new_gunpla():
    """Test creating a new Gunpla instance."""
    gunpla = Gunpla(
        name='RX-78-2',
        series='Mobile Suit Gundam',
        grade='MG',
        scale='1/100'
    )
    assert gunpla.name == 'RX-78-2'
    assert gunpla.series == 'Mobile Suit Gundam'
    assert gunpla.grade == 'MG'
    assert gunpla.scale == '1/100'

def test_gunpla_representation():
    """Test the string representation of a Gunpla instance."""
    gunpla = Gunpla(name='RX-78-2')
    assert str(gunpla) == '<Gunpla RX-78-2>'

def test_gunpla_db_interaction(app):
    """Test database interactions with Gunpla model."""
    # Create and add a new Gunpla
    gunpla = Gunpla(
        name='Unicorn',
        series='Mobile Suit Gundam Unicorn',
        grade='PG',
        scale='1/60'
    )
    db.session.add(gunpla)
    db.session.commit()
    
    # Query and verify
    saved_gunpla = Gunpla.query.first()
    assert saved_gunpla.name == 'Unicorn'
    assert saved_gunpla.id is not None