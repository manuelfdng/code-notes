# Django Gunpla API

A simple RESTful API built with Django and Django REST Framework for managing Gunpla model kit information.

## Overview

This application provides a backend API for tracking Gunpla model kits, storing information such as:
- Name (e.g., "RX-78-2 Gundam")
- Series (e.g., "Mobile Suit Gundam")
- Grade (e.g., "Master Grade")
- Scale (e.g., "1/100")

The API allows users to perform standard CRUD (Create, Read, Update, Delete) operations on Gunpla model data.

## Project Structure

```
django-gunpla-backend-only/
└── myproject/
    ├── manage.py                  # Django command-line utility
    ├── gunpla/                    # Main application
    │   ├── __init__.py
    │   ├── admin.py               # Admin panel configuration
    │   ├── apps.py                # App configuration
    │   ├── models.py              # Database models
    │   ├── serializers.py         # JSON serializers
    │   ├── tests.py               # API tests
    │   └── views.py               # API views
    └── myproject/                 # Project settings
        ├── __init__.py
        ├── asgi.py                # ASGI configuration
        ├── settings.py            # Project settings
        ├── urls.py                # URL routing
        └── wsgi.py                # WSGI configuration
```

## Key Components

### Models (`gunpla/models.py`)

Defines the `Gunpla` model with the following fields:
- `name`: The name of the Gunpla model
- `series`: The anime/media series the Gunpla is from
- `grade`: The grade of the model (e.g., High Grade, Master Grade)
- `scale`: The scale of the model (e.g., 1/144, 1/100)

### Serializers (`gunpla/serializers.py`)

Handles the conversion between Python objects and JSON, with field validation:
- Enforces required fields (name, series, grade)
- Formats data for API responses

### Views (`gunpla/views.py`)

Implements the API endpoints using Django REST Framework's `APIView`:
- `GunplaList`: Handles GET (list all) and POST (create) operations
- `GunplaDetail`: Handles GET (single item), PUT (update), and DELETE operations

### URLs (`myproject/urls.py`)

Maps URLs to views:
- `/gunplas`: List all Gunpla models or create new ones
- `/gunplas/<id>`: Retrieve, update, or delete a specific Gunpla model

### Tests (`gunpla/tests.py`)

Comprehensive test suite that verifies:
- Listing Gunpla models (empty and populated database)
- Creating Gunpla models (with valid and invalid data)
- Retrieving specific Gunpla models
- Updating Gunpla models
- Deleting Gunpla models
- Error handling for non-existent resources

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/gunplas` | GET | List all Gunpla models |
| `/gunplas` | POST | Create a new Gunpla model |
| `/gunplas/<id>` | GET | Retrieve a specific Gunpla model |
| `/gunplas/<id>` | PUT | Update a specific Gunpla model |
| `/gunplas/<id>` | DELETE | Delete a specific Gunpla model |

## Getting Started

1. Clone the repository
2. Install dependencies:
   ```
   pip install django djangorestframework
   ```
3. Navigate to the project directory:
   ```
   cd django-gunpla-backend-only/myproject
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```
6. Access the API at `http://localhost:8000/gunplas`

## Running Tests

To run the test suite:

```
python manage.py test gunpla
```