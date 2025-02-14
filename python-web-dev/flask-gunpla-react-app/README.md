# Gunpla Frontend

Welcome to the Gunpla Frontend! This is a React application built with Vite that serves as a user-friendly interface to interact with the Flask-based Gunpla API. Whether you're new to React or just looking to learn how to build a modern frontend, this project will help you understand the basics of React, Vite, and state management with React Context.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)

## Overview

The Gunpla Frontend is designed to work with the Flask-based Gunpla API to let you:
- **View** a list of Gunpla models.
- **Add** a new Gunpla model.
- **Edit** existing Gunpla models.
- **Delete** Gunpla models.

This application is built using React functional components, React hooks for state management, and React Context to manage global state. Vite is used as the build tool for a fast and modern development experience.

## Features

- **Modern React Setup:** Uses React 18, functional components, and hooks.
- **State Management:** Utilizes React Context to manage application state.
- **API Integration:** Connects seamlessly with the Flask API via proxy settings in Vite.
- **Responsive UI:** A simple and clean interface to perform CRUD operations.
- **Development Convenience:** Built with Vite for fast rebuilds and an optimized development experience.

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

- [Node.js](https://nodejs.org/) (v14 or higher is recommended)
- npm (comes with Node.js) or yarn
- A running instance of the Flask-based Gunpla API (by default running on [http://localhost:5000](http://localhost:5000))

## Installation

Follow these steps to get your development environment set up:

1. **Clone the Repository:**

    ```bash
    git clone https://your-repo-url.git
    cd gunpla-frontend
    ```

2.	Install Dependencies:

    Using npm:

    ```bash
    npm install
    ```

    Or using yarn:

    ```bash
    yarn
    ```


## Configuration

The application uses Vite’s environment variables and a proxy configuration to communicate with the Flask API. By default, the Vite dev server is configured to proxy requests from /gunplas to http://localhost:5000.

If you need to change the API URL, you can create a .env file in the root of the project and define the following variable:

```
VITE_API_URL=http://localhost:5000
```

This will override the default API endpoint if needed.

## Running the Application

### Development Server

To start the development server, run:

Using npm:

```bash
npm run dev
```

Or using yarn:

```bash
yarn dev
```

This will launch the Vite development server, and you can view the app in your browser at http://localhost:5173.

## Production Build

To create an optimized production build, run:

Using npm:

```bash
npm run build
```

Or using yarn:

```bash
yarn build
```

You can preview the production build locally with:

Using npm:

```bash
npm run preview
```

Or using yarn:

```bash
yarn preview
```

## Project Structure

```
gunpla-frontend/
├── node_modules/             # Installed dependencies
├── public/                   # Public assets (e.g., favicon)
├── src/
│   ├── components/           # Reusable React components
│   │   ├── GunplaForm.jsx    # Form component for adding/editing models
│   │   ├── GunplaItem.jsx    # Single gunpla item component
│   │   └── GunplaList.jsx    # List component to display all gunpla models
│   ├── context/              # React Context for state management
│   │   └── GunplaContext.jsx # Context provider and logic for managing gunpla data
│   ├── App.jsx               # Main application component
│   ├── main.jsx              # Application entry point
│   └── index.css             # Global styles
├── .env                      # Optional: Environment variables (e.g., VITE_API_URL)
├── package.json              # Project metadata and scripts
├── vite.config.js            # Vite configuration, including API proxy setup
└── README.md                 # This file
```

## How It Works
1.	React Context: The application state is managed using React Context (GunplaContext.jsx). This context holds the list of Gunpla models, loading state, error messages, and functions to add, update, or delete models.

2. Components:
- GunplaForm.jsx: Handles both adding new Gunpla models and editing existing ones using controlled form inputs.
- GunplaList.jsx & GunplaItem.jsx: Display the list of Gunpla models. Each item has options to edit or delete the model.

3. API Integration: API calls are made to the Flask backend (proxied by Vite) to perform CRUD operations. The proxy setup in vite.config.js ensures that any call to /gunplas is forwarded to the Flask API.




