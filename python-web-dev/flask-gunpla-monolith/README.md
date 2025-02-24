# Gunpla Manager - Flask Monolith Application

A traditional server-side rendered web application for managing Gunpla model collections, built with Flask and SQLAlchemy. This application provides a straightforward interface for maintaining a database of Gunpla models with full CRUD functionality.

## Overview

The Gunpla Manager is a monolithic Flask application that follows traditional web development patterns, using server-side rendering with Jinja2 templates. The application allows users to create, view, update, and delete Gunpla model entries in a simple and efficient manner.

## Tech Stack

- **Flask**: Web framework
- **SQLAlchemy**: ORM for database operations
- **Flask-WTF**: Form handling and CSRF protection
- **Flask-Migrate**: Database migrations
- **SQLite**: Database backend
- **Jinja2**: Template engine
- **pytest**: Testing framework

## Project Structure

```
flask-gunpla-monolith/
├── config.py                # Application configuration
├── run.py                  # Application entry point
└── app/                    # Main application package
    ├── forms/              # WTForms form definitions
    ├── models/             # SQLAlchemy models
    ├── routes/             # Route handlers
    ├── static/             # Static assets (CSS)
    ├── templates/          # Jinja2 templates
    └── tests/              # Test suite
```

## Key Components

### Backend Components

#### Models (`app/models/`)
- `gunpla.py`: Defines the Gunpla model with fields for:
  - Name (required)
  - Series (required)
  - Grade (required)
  - Scale (optional)

#### Forms (`app/forms/`)
- `gunpla.py`: Form definitions using Flask-WTF for:
  - Creating new Gunpla entries
  - Editing existing entries
  - Input validation

#### Routes (`app/routes/`)
- `main.py`: Route handlers for:
  - Listing all Gunpla models
  - Creating new entries
  - Editing existing entries
  - Deleting entries

### Frontend Components

#### Templates (`app/templates/`)
- `base.html`: Base template with common layout elements
- `gunpla/`:
  - `index.html`: Main listing page
  - `create.html`: Creation form
  - `edit.html`: Edit form

#### Static Files (`app/static/`)
- `css/style.css`: Basic styling for the application

## Features

- **Model Management**: Full CRUD operations for Gunpla models
- **Form Validation**: Server-side validation with error messages
- **Flash Messages**: User feedback for actions
- **CSRF Protection**: Secure form submissions
- **Responsive Design**: Basic mobile-friendly layout
- **Database Integration**: SQLite backend with SQLAlchemy ORM

## Development Setup

1. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize database**
   ```bash
   flask db upgrade
   ```

4. **Run the application**
   ```bash
   python run.py
   ```

## Testing

The application includes a comprehensive test suite using pytest:

```bash
pytest
```

Test coverage includes:
- Form validation tests
- Model operations
- Route handling
- Database interactions

## Routes

- `GET /`: Main index page displaying all Gunpla models
- `GET/POST /create`: Gunpla creation form and handling
- `GET/POST /edit/<id>`: Edit form and handling for existing Gunpla
- `POST /delete/<id>`: Delete existing Gunpla

## Security Features

- CSRF protection on all forms
- Input validation and sanitization
- Secure database operations
- Error handling and 404 pages
- SQL injection prevention through SQLAlchemy

## Database Schema

The Gunpla model includes the following fields:
- `id`: Integer, Primary Key
- `name`: String(100), Required
- `series`: String(100), Required
- `grade`: String(50), Required
- `scale`: String(20), Optional