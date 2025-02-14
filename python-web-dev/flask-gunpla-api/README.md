# Gunpla API

A simple CRUD API for managing Gunpla models, built using Flask-RESTful, Flask-SQLAlchemy, and SQLite. This API supports Create, Read, Update, and Delete (CRUD) operations with a modular and maintainable project structure.

## 📁 Project Structure

```
gunpla_api/
├── app.py         # Main application file that creates and runs the Flask app.
├── config.py      # Configuration settings (database URI, debug mode, etc.).
├── models.py      # SQLAlchemy model(s) and database initialization.
├── resources.py   # Flask-RESTful resources (endpoints) for Gunpla models.
└── test.py        # Pytest-based test suite covering key API functionalities.
```

## 📌 Requirements
	•	Python 3.7 or higher
	•	Flask
	•	Flask-RESTful
	•	Flask-SQLAlchemy
	•	Pytest (for testing)

## 🚀 Setup

1️⃣ Clone the Repository

```bash
git clone https://your-repo-url.git
cd gunpla_api
```

2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the virtual environment:
- On macOS/Linux:

```bash
source venv/bin/activate
```

- On Windows:

```cmd
venv\Scripts\activate
```

##3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

The application configuration is located in config.py. By default, the API uses a SQLite database (gunpla.db) in the project directory.

You can adjust settings such as:
- Debug mode
- Database URI

## ▶️ Running the Application

Start the API server with:

```bash
python app.py
```

By default, the API will be available at:

http://localhost:5000

📡 API Endpoints

## 🔹 Gunpla Models

| Method | Endpoint              | Description                       |
|--------|-----------------------|-----------------------------------|
| GET    | `/gunplas`            | Retrieve a list of all Gunpla models. |
| POST   | `/gunplas`            | Create a new Gunpla model.        |
| GET    | `/gunplas/<gunpla_id>`| Retrieve a specific Gunpla model. |
| PUT    | `/gunplas/<gunpla_id>`| Update an existing Gunpla model.  |
| DELETE | `/gunplas/<gunpla_id>`| Delete a specific Gunpla model.   |

## 📤 Example Payloads

### ➕ Create a Gunpla

```
POST /gunplas

{
  "name": "RX-78-2 Gundam",
  "series": "Mobile Suit Gundam",
  "grade": "High Grade",
  "scale": "1/144"
}
```

### 🔄 Update a Gunpla

```
PUT /gunplas/<gunpla_id>

{
  "name": "RX-78-2 Gundam (Updated)",
  "series": "Mobile Suit Gundam",
  "grade": "Master Grade",
  "scale": "1/100"
}
```

## 🧪 Testing

Tests are written using pytest. Run the test suite with:

```bash
pytest test.py
```

### 🎯 Notes
- This project uses Session.get() instead of Query.get(), avoiding legacy warnings in SQLAlchemy.
- If you encounter any issues, ensure that your virtual environment is activated and all dependencies are installed.

Happy building! 🏗️✨