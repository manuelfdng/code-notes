# Gunpla Manager Application

A full-stack web application for managing Gunpla model collections, built with Flask (Backend) and React (Frontend). The application allows users to create, read, update, and delete Gunpla model entries, including information such as model name, series, grade, and scale.

## Overview

This application provides a user-friendly interface for Gunpla enthusiasts to maintain their model collection database. Each Gunpla entry contains essential information about the model kit, and users can perform all CRUD operations through an intuitive web interface.

## Tech Stack

### Backend
- **Flask**: Python web framework
- **Flask-RESTful**: REST API framework
- **SQLAlchemy**: SQL toolkit and ORM
- **SQLite**: Database

### Frontend
- **React**: UI library
- **Vite**: Build tool and development server
- **Vitest**: Testing framework
- **MSW**: API mocking for tests

## Project Structure

### Backend (`/backend`)

```
backend/
├── run.py                 # Application entry point
├── app/                   # Main application package
│   ├── api/              # API routes and resources
│   ├── models/           # Database models
│   └── utils/            # Utility functions
├── config/               # Configuration settings
└── tests/                # Test suite
```

#### Key Backend Files

- `run.py`: Server entry point that initializes and runs the Flask application
- `app/__init__.py`: Application factory and configuration
- `app/api/routes.py`: API endpoint definitions and request handling
- `app/models/gunpla.py`: Gunpla data model and database schema
- `app/utils/request_parser.py`: Request validation and parsing utilities

### Frontend (`/frontend`)

```
frontend/
├── index.html            # Entry HTML file
├── src/                  # Source code directory
│   ├── App.jsx          # Root component
│   ├── api/             # API client functions
│   ├── components/      # React components
│   ├── context/         # React context definitions
│   └── styles/          # CSS styles
└── tests/               # Component tests
```

#### Key Frontend Files

- `src/App.jsx`: Main application component
- `src/api/gunplaApi.js`: API client functions for backend communication
- `src/components/gunpla/`: Gunpla-related components
  - `GunplaForm.jsx`: Form for creating/editing Gunpla entries
  - `GunplaList.jsx`: Display list of Gunpla entries
  - `GunplaItem.jsx`: Individual Gunpla entry component
- `src/context/GunplaContext.jsx`: Global state management
- `src/styles/index.css`: Global styles

## Features

- **Create Gunpla Entries**: Add new Gunpla models with details
- **View Gunpla List**: Display all stored Gunpla models
- **Update Entries**: Modify existing Gunpla information
- **Delete Entries**: Remove Gunpla models from the database
- **Form Validation**: Ensure required fields are filled
- **Error Handling**: Display user-friendly error messages
- **Loading States**: Show loading indicators during API calls

## Development Setup

1. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   python run.py
   ```

2. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## API Endpoints

- `GET /gunplas`: Retrieve all Gunpla models
- `POST /gunplas`: Create a new Gunpla model
- `GET /gunplas/<id>`: Retrieve a specific Gunpla model
- `PUT /gunplas/<id>`: Update a specific Gunpla model
- `DELETE /gunplas/<id>`: Delete a specific Gunpla model