# tests/unit/test_forms.py
import pytest
from app.forms.gunpla import GunplaForm

def test_valid_gunpla_form(app):
    """Test form validation with valid data"""
    with app.test_request_context():
        form = GunplaForm(
            formdata=None,
            name='Wing Gundam',
            series='Gundam Wing',
            grade='MG',
            scale='1/100'
        )
        assert form.validate() == True

def test_invalid_gunpla_form(app):
    """Test form validation with missing required fields"""
    with app.test_request_context():
        form = GunplaForm(
            formdata=None,
            name='',  # Required field is empty
            series='Gundam Wing',
            grade='MG',
            scale='1/100'
        )
        assert form.validate() == False
        assert 'This field is required.' in form.name.errors