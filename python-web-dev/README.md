# Python Web Rendering Patterns

This repository contains notes and sample applications illustrating **three primary approaches** to building web applications in Python. These approaches focus on **how content is rendered**—from traditional server-side rendering (SSR) in Flask, to partial dynamic updates with HTMX, and finally to a full client-side React frontend that communicates with a Flask API.

## Table of Contents

- [Overview of Rendering Patterns](#overview-of-rendering-patterns)
  - [1. Traditional Server-Side Rendering (Flask)](#1-traditional-server-side-rendering-flask)
  - [2. Server-Side Rendering with HTMX (Flask + HTMX)](#2-server-side-rendering-with-htmx-flask--htmx)
  - [3. Single-Page Application (Flask + React)](#3-single-page-application-flask--react)
- [Why Different Rendering Approaches?](#why-different-rendering-approaches)
- [Project Structure](#project-structure)
- [How to Run Each Project](#how-to-run-each-project)
---

## Overview of Rendering Patterns

### 1. Traditional Server-Side Rendering (Flask)

**Project:** [flask-gunpla-monolith/](../flask-gunpla-monolith/)

In **server-side rendering** (SSR), each request to the server results in a new HTML page being generated on the backend. The Flask application:

- Renders HTML templates via [Jinja2](https://jinja.palletsprojects.com/).
- Performs all create/read/update/delete (CRUD) operations on the server side.
- Sends fully-formed HTML responses back to the client.

**Pros:**

- Simpler data flow: The client just makes requests; the server handles everything and responds with complete HTML.
- Great for SEO (search engine optimization), as content is rendered on the server.
- Minimal JavaScript complexity—ideal for smaller applications or simple dynamic needs.

**Cons:**

- Page reloads for every interaction or form submission.
- Harder to provide a “real-time” or “snappier” user experience without adding heavier front-end code or partial-refresh techniques.

---

### 2. Server-Side Rendering with HTMX (Flask + HTMX)

**Project:** [flask-gunpla-monolith-htmx/](../flask-gunpla-monolith-htmx/)

This approach still uses **server-side rendering** but enhances it with **[HTMX](https://htmx.org/)** to perform **partial page updates**. Instead of doing a full page reload for every user action:

- Certain elements are updated in place (e.g., editing a single list item, deleting a record, or dynamically swapping out form elements).
- HTMX handles the network requests automatically, sending or receiving small fragments of HTML.
- JavaScript is minimal: HTMX is declarative, so you mostly configure it in your HTML attributes.

**Pros:**

- Faster, more interactive UI without building a full single-page app.
- Less JavaScript overhead: HTMX dynamically fetches or posts to server endpoints and seamlessly replaces parts of the DOM.
- Simple transitions from purely SSR-based templates to partial, dynamic updates.

**Cons:**

- Still server-bound: no full offline capability or large-scale front-end logic as you might have in a React/Vue/Angular SPA.
- If your application requirements grow complex, you might end up mixing various front-end solutions.

---

### 3. Single-Page Application (Flask + React)

**Project:** [flask-react-gunpla-app/](../flask-react-gunpla-app/)

In this pattern, **React** handles all the client-side rendering, and Flask provides a **RESTful API**:

- The React app (bundled with tools like [Vite](https://vitejs.dev/)) makes AJAX/Fetch requests to the Flask API.
- The Flask API (using [Flask-RESTful](https://flask-restful.readthedocs.io/)) provides JSON responses.
- The frontend manages state, routing, and views entirely in the browser.

**Pros:**

- Very responsive, “app-like” user experience with no full-page reloads.
- Clear separation of concerns: the backend is purely an API, the frontend is purely a React SPA.
- Flexible scaling if you want to switch your backend or integrate with other microservices.

**Cons:**

- Higher complexity: you must maintain and deploy two separate codebases (front-end and back-end).
- SEO requires extra consideration (e.g., SSR for React or frameworks like Next.js if search-engine indexing is critical).
- Steeper learning curve for those new to front-end frameworks and tooling.

---

## Why Different Rendering Approaches?

Each approach serves different needs:

- **Full SSR** is straightforward and suitable for smaller projects or those where SEO is critical and minimal dynamic interactions are needed.
- **SSR + HTMX** is a great middle ground—still server-focused but with interactive elements that don’t require a full JavaScript SPA.
- **SPA (React)** is often chosen for richer, highly interactive applications that might be extended to mobile apps, multi-page flows, or need advanced client-side logic.

---

## Project Structure

This repository has a top-level folder, **`python-web-dev/`**, containing three main subdirectories, each illustrating a different rendering pattern:

```
python-web-dev/
├── flask-gunpla-monolith/        # (1) Flask SSR
├── flask-gunpla-monolith-htmx/   # (2) Flask SSR with HTMX
├── flask-react-gunpla-app/       # (3) Flask + React SPA
└── notes/
    ├── django-commands.md
    ├── python-features.md
    └── rendering-patterns.md  
```

Each sub-project has its own `README.md`, its own `run.py` or equivalent entry point, and its own set of dependencies.

---

## How to Run Each Project

### 1. Flask Gunpla Monolith (Server-Side Rendering)

1. **Install Requirements**  
   ```bash
   cd flask-gunpla-monolith
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. **Set Up Database** (optional, if you’d like to run migrations)  
   ```bash
   flask db upgrade
   ```
3. **Run App**  
   ```bash
   python run.py
   ```
4. Open your browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

### 2. Flask Gunpla Monolith HTMX (SSR + HTMX)

1. **Install Requirements**  
   ```bash
   cd flask-gunpla-monolith-htmx
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Run App**  
   ```bash
   python run.py
   ```
3. Open your browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

You will see dynamic interactions (inline edits, partial refreshes, etc.) powered by HTMX.

---

### 3. Flask-React Gunpla App (SPA)

**Backend Setup:**

1. **Install Requirements**  
   ```bash
   cd flask-react-gunpla-app/backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Run Flask Server**  
   ```bash
   python run.py
   ```
3. The Flask server will run at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

**Frontend Setup:**

1. **Install NPM Dependencies**  
   ```bash
   cd ../frontend
   npm install
   ```
2. **Run React Dev Server**  
   ```bash
   npm run dev
   ```
3. The React client runs at [http://127.0.0.1:5173/](http://127.0.0.1:5173/) (or a similar port). It proxies API requests to the Flask backend.

---

**Happy Building!**  
Use these projects and notes as a guide to explore the trade-offs of different rendering patterns, from traditional SSR to modern single-page apps. Experiment and choose the approach that best suits your project’s size, complexity, and user experience requirements.