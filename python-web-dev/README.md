# Python Web Development Examples

This repository demonstrates different approaches to building web applications with Python, focusing on various rendering patterns and architectures. It includes examples of traditional server-side rendering, modern HTML-over-the-wire techniques with HTMX, and a full-stack application using React.

## Repository Structure

```
python-web-dev/
├── django-commands.md
├── python-features.md
├── rendering-patterns.md
├── flask-gunpla-monolith/        # Traditional Flask Monolith
├── flask-gunpla-monolith-htmx/   # Flask + HTMX Implementation
└── flask-react-gunpla-app/       # Flask + React Full-Stack App
```

## Applications

All three applications implement the same Gunpla (Gundam plastic model) management system with basic CRUD operations, each using a different architectural approach:

### 1. Traditional Flask Monolith
- Located in `flask-gunpla-monolith/`
- Uses traditional server-side rendering with full page reloads
- Features:
  - SQLAlchemy for database management
  - WTForms for form handling and validation
  - Jinja2 templates for rendering
  - CSRF protection
  - Complete test suite

### 2. Flask + HTMX Implementation
- Located in `flask-gunpla-monolith-htmx/`
- Modern HTML-over-the-wire approach
- Features:
  - Same backend structure as the monolith
  - HTMX for dynamic updates without full page reloads
  - Partial template rendering
  - Enhanced user experience with smoother interactions
  - Maintains simplicity of server-side rendering

### 3. Flask + React Full-Stack Application
- Located in `flask-react-gunpla-app/`
- Modern decoupled architecture
- Features:
  - Flask RESTful API backend
  - React frontend with Vite
  - Context API for state management
  - Proxy configuration for development
  - Complete separation of concerns

## Documentation Files

- `django-commands.md`: Quick reference for common Django commands and notes on differences from Flask
- `python-features.md`: General Python programming notes
- `rendering-patterns.md`: Documentation on web rendering approaches

## Setup and Running

### Backend (All Versions)
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run Flask application
python app.py
```

### Frontend (React Version)
```bash
cd flask-react-gunpla-app/frontend

# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build
```

## Testing

Each application includes a comprehensive test suite. Run tests using:

```bash
python -m pytest test.py
```

## Key Features Across All Implementations

- SQLite database using SQLAlchemy
- CRUD operations for Gunpla models
- Form validation
- Error handling
- Flash messages for user feedback
- Responsive design
- Comprehensive testing

## Learning Objectives

This repository demonstrates:
1. Different web application architectures
2. Progressive enhancement with HTMX
3. Full-stack development with React
4. Flask application patterns and best practices
5. Modern frontend development approaches
6. Testing strategies for web applications

## Technology Stack

### Common Backend (All Versions)
- Flask
- SQLAlchemy
- SQLite
- WTForms
- Python unittest/pytest

### Frontend Technologies
- Traditional: Jinja2 Templates
- HTMX Version: HTMX + Jinja2
- Modern: React + Vite

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available for learning purposes.