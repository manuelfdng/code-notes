# tests/unit/test_models.py
import pytest
from app.models.gunpla import Gunpla

def test_new_gunpla():
    """Test creating a new Gunpla model"""
    gunpla = Gunpla(
        name='Unicorn Gundam',
        series='Gundam UC',
        grade='PG',
        scale='1/60'
    )
    assert gunpla.name == 'Unicorn Gundam'
    assert gunpla.series == 'Gundam UC'
    assert gunpla.grade == 'PG'
    assert gunpla.scale == '1/60'

def test_gunpla_representation():
    """Test the string representation of Gunpla model"""
    gunpla = Gunpla(name='Strike Freedom')
    assert str(gunpla) == '<Gunpla Strike Freedom>'