# Gunpla Manager - Flask & HTMX Application

A modern monolithic web application for managing Gunpla model collections, built with Flask and HTMX. This application provides a responsive, dynamic user interface for managing Gunpla models without the complexity of a separate frontend framework.

## Overview

The Gunpla Manager is a server-side rendered application that uses HTMX to provide dynamic updates and interactions without writing custom JavaScript. Users can create, read, update, and delete Gunpla model entries with smooth, partial page updates.

## Tech Stack

- **Flask**: Python web framework
- **SQLAlchemy**: ORM for database operations
- **Flask-WTF**: Form handling and CSRF protection
- **HTMX**: Frontend interactivity without JavaScript
- **Flask-Migrate**: Database migrations
- **SQLite**: Database backend

## Project Structure

```
flask-gunpla-monolith-htmx/
├── config.py                # Application configuration
├── run.py                  # Application entry point
└── app/                    # Main application package
    ├── forms/              # WTForms form definitions
    ├── models/             # SQLAlchemy models
    ├── routes/             # Route handlers
    ├── static/             # Static assets (CSS, JS)
    ├── templates/          # Jinja2 templates
    └── tests/              # Test suite
```

## Key Components

### Backend Components

#### Models (`app/models/`)
- `gunpla.py`: Defines the Gunpla database model with fields for name, series, grade, and scale

#### Forms (`app/forms/`)
- `gunpla.py`: WTForms definitions for Gunpla creation and editing

#### Routes (`app/routes/`)
- `main.py`: Route handlers for all CRUD operations and HTMX interactions

### Frontend Components

#### Templates (`app/templates/`)
- `base.html`: Base template with common layout and HTMX setup
- `gunpla/`:
  - `index.html`: Main listing page
  - `create.html`: Form for creating new entries
  - `edit_form.html`: HTMX-powered inline editing form
  - `gunpla_row.html`: Individual Gunpla entry template

#### Static Files (`app/static/`)
- `css/style.css`: Application styling
- `js/htmx-csrf.js`: CSRF token handling for HTMX requests

## Features

- **Server-Side Rendering**: Fast initial page loads with proper SEO support
- **Dynamic Updates**: HTMX-powered partial page updates for a smooth user experience
- **Inline Editing**: Edit Gunpla entries without page reloads
- **Form Validation**: Server-side validation with immediate feedback
- **Flash Messages**: User feedback for successful operations
- **CSRF Protection**: Secure form submissions and HTMX requests

## HTMX Integration

The application leverages HTMX for dynamic interactions:

- Inline editing of Gunpla entries
- Dynamic deletion with confirmation
- Partial page updates for form submissions
- Automatic CSRF token handling
- Flash message management

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

Run the test suite using pytest:
```bash
pytest
```

Test coverage includes:
- Form validation
- Model operations
- Route handling
- HTMX interactions

## API Routes

- `GET /`: Main index page with Gunpla listing
- `GET/POST /create`: Gunpla creation
- `GET/POST /edit/<id>`: Edit existing Gunpla
- `POST /delete/<id>`: Delete Gunpla
- `GET /gunpla/<id>/edit-form`: Get HTMX edit form
- `GET /gunpla/<id>`: Get single Gunpla row