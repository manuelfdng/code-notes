# tests/test_forms.py
import pytest
from flask import Flask
from app.forms.gunpla import GunplaForm

def test_valid_gunpla_form(app):
    """Test form validation with valid data."""
    with app.test_request_context():
        form = GunplaForm(
            name='Exia',
            series='Gundam 00',
            grade='RG',
            scale='1/144'
        )
        assert form.validate() is True

def test_invalid_gunpla_form(app):
    """Test form validation with missing required fields."""
    with app.test_request_context():
        form = GunplaForm(
            name='',  # Required field
            series='Gundam 00',
            grade='RG',
            scale='1/144'
        )
        assert form.validate() is False
        assert 'This field is required.' in form.name.errors

def test_optional_scale_field(app):
    """Test that scale field is optional."""
    with app.test_request_context():
        form = GunplaForm(
            name='Exia',
            series='Gundam 00',
            grade='RG',
            scale=''  # Optional field
        )
        assert form.validate() is True