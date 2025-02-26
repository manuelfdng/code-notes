# Gunpla Frontend (React App)

Welcome to the **Gunpla Frontend**! This README is designed for someone who already knows **Python** but is new to **React**. We'll draw analogies to Python as we go along to make the React concepts more approachable.

## Table of Contents

1. [Overview](#overview)
2. [Directory Structure](#directory-structure)
3. [React Fundamentals](#react-fundamentals)
    - [Components](#components)
    - [Props](#props)
    - [State](#state)
    - [Lifecycle & `useEffect`](#lifecycle--useeffect)
    - [Context](#context)
4. [Walkthrough of This App](#walkthrough-of-this-app)
    - [Key Files Explained](#key-files-explained)
        - [`App.jsx`](#appjsx)
        - [`GunplaContext.jsx` (Context Provider)](#gunplacontextjsx-context-provider)
        - [`GunplaForm.jsx`](#gunplaformjsx)
        - [`GunplaList.jsx` & `GunplaItem.jsx`](#gunpalistjsx--gunplaitemjsx)
        - [`gunplaApi.js`](#gunplaapijs)
        - [`setupTests.js`, `testUtils.jsx`](#setuptestsjs-testutilsjsx)
5. [Running the App](#running-the-app)
6. [Testing](#testing)

---

## Overview

This is a simple CRUD (Create, Read, Update, Delete) application built with **React**. It manages a list of Gunpla models (Gundam plastic models). At a high level:

- **Frontend** (React) communicates with an API (mocked by the library [MSW](https://mswjs.io/) in testing).
- Uses React's **Context** to store the Gunpla data and provide it to components.
- Handles forms to add and edit Gunpla information, a list to display them, and allows deleting an existing model.

If you think of Python, you might imagine a typical Django or Flask project where you have:

- **Views** (for user interaction),
- **Templates** (for the UI),
- **Models** (for data).

In React, our “**views**” and “**templates**” combine into **components**. These components can also manage internal data (state) or access external data via context or props.

---

## Directory Structure

Below is the relevant structure of the `frontend/` folder. The important files for you as a React beginner are the `.jsx` and `.js` files:

```
frontend/
├── index.html
├── package.json
├── vite.config.js
└── src/
    ├── App.jsx
    ├── main.jsx
    ├── setupTests.js
    ├── test-utils.jsx
    ├── testUtils.jsx
    ├── api/
    │   └── gunplaApi.js
    ├── components/
    │   ├── common/
    │   │   ├── ErrorMessage.jsx
    │   │   └── LoadingSpinner.jsx
    │   └── gunpla/
    │       ├── GunplaForm.jsx
    │       ├── GunplaItem.jsx
    │       ├── GunplaList.jsx
    │       └── __tests__/
    │           ├── GunplaForm.test.jsx
    │           ├── GunplaItem.test.jsx
    │           └── GunplaList.test.jsx
    ├── context/
    │   └── GunplaContext.jsx
    └── styles/
        └── index.css
```

---

## React Fundamentals

### Components

- **Components** are the building blocks of a React application. You can think of them like Python functions or classes that produce HTML (or the UI).
- A component is typically written in a `.jsx` file and is **capitalized** (e.g., `GunplaForm.jsx`).

In Python, you might have a function returning a string that is rendered on a web page. In React, a component **returns** JSX (JavaScript XML) that the browser renders.

```jsx
function ExampleComponent() {
  return (
    <div>Hello from ExampleComponent!</div>
  );
}
```

### Props

- **Props** (short for properties) are how data is passed **into** a component from a parent.
- In Python terms, it’s like calling a function with parameters. Those parameters are how you pass external data into that function.

For example:

```jsx
function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
}

// Using the Greeting component:
<Greeting name="Alice" />
```

### State

- **State** is internal data managed by a component (or by a hook like `useState`).
- In Python, you might store local variables in a function or maintain object attributes in a class. React’s **state** is the way to store data that triggers a re-render when changed.

Example of using state:

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);  // Initialize state

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

### Lifecycle & `useEffect`

- In Python classes, you have methods like `__init__`, and in Django or Flask, you might have request lifecycle hooks or signals.
- In React, **hooks** like `useEffect` let you run code at certain times in a component’s lifecycle (e.g., **on mount**, **on update**, **on unmount**).

Example:

```jsx
function Example() {
  const [data, setData] = useState(null);

  useEffect(() => {
    // Runs after the component is rendered to the DOM
    fetchData().then(res => setData(res));
  }, []);  // The empty array means this effect runs only once on mount

  return <div>{data ? data : 'Loading...'}</div>;
}
```

### Context

- **Context** in React allows you to **share** data across multiple components **without** having to pass props down manually at every level.
- Think of it like a Python **global object** or a **Django context processor** that any template can access. But in React, it's more structured.

In our app, we use a **GunplaContext** to store all Gunpla data and share it.

---

## Walkthrough of This App

### Key Files Explained

#### `App.jsx`

```jsx
import React from 'react';
import GunplaForm from './components/gunpla/GunplaForm';
import GunplaList from './components/gunpla/GunplaList';

function App() {
  return (
    <div style={{ maxWidth: '800px', margin: '0 auto', padding: '1rem' }}>
      <h1>Gunpla Models Manager</h1>
      <GunplaForm />
      <GunplaList />
    </div>
  );
}

export default App;
```

- **`App`** is the “root” component. 
- It just **renders** a title, a form for adding/editing Gunpla, and the list of Gunpla.

#### `GunplaContext.jsx` (Context Provider)

```jsx
import React, { createContext, useState, useEffect } from 'react';
import { 
    fetchGunplas as apiFetchGunplas,
    createGunpla,
    updateGunpla as apiUpdateGunpla,
    deleteGunpla as apiDeleteGunpla
} from '../api/gunplaApi';

export const GunplaContext = createContext();

export const GunplaProvider = ({ children }) => {
    const [gunplas, setGunplas] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [selectedGunpla, setSelectedGunpla] = useState(null);

    const fetchGunplas = async () => {
        setLoading(true);
        setError(null);
        try {
            const data = await apiFetchGunplas();
            setGunplas(data);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    const addGunpla = async (gunpla) => {
        setError(null);
        try {
            const data = await createGunpla(gunpla);
            setGunplas(prev => [...prev, data]);
        } catch (err) {
            setError(err.message);
            throw err;
        }
    };

    const updateGunpla = async (id, updatedGunpla) => {
        setError(null);
        try {
            const data = await apiUpdateGunpla(id, updatedGunpla);
            setGunplas(prev => prev.map(g => (g.id === id ? data : g)));
        } catch (err) {
            setError(err.message);
            throw err;
        }
    };

    const deleteGunpla = async (id) => {
        setError(null);
        try {
            await apiDeleteGunpla(id);
            setGunplas(prev => prev.filter(g => g.id !== id));
        } catch (err) {
            setError(err.message);
            throw err;
        }
    };

    useEffect(() => {
        fetchGunplas();
    }, []);

    return (
        <GunplaContext.Provider value={{
            gunplas,
            loading,
            error,
            fetchGunplas,
            addGunpla,
            updateGunpla,
            deleteGunpla,
            selectedGunpla,
            setSelectedGunpla
        }}>
            {children}
        </GunplaContext.Provider>
    );
};
```

- We create a context called `GunplaContext`.
- `GunplaProvider` **fetches** Gunpla from our API on mount (via `useEffect`).
- It provides state (`gunplas`, `loading`, `error`, `selectedGunpla`) and **actions** (`fetchGunplas`, `addGunpla`, `updateGunpla`, `deleteGunpla`, `setSelectedGunpla`) to any component that needs them.

This is similar to having a Python class that loads data from a database and shares it with multiple routes. But in React, we wrap children components in this context.

#### `GunplaForm.jsx`

```jsx
import React, { useState, useContext, useEffect } from 'react';
import { GunplaContext } from '../../context/GunplaContext';
import ErrorMessage from '../common/ErrorMessage';

const initialFormState = {
    name: '',
    series: '',
    grade: '',
    scale: ''
};

function GunplaForm() {
    const { addGunpla, updateGunpla, selectedGunpla, setSelectedGunpla, error } = useContext(GunplaContext);
    const [formData, setFormData] = useState(initialFormState);

    useEffect(() => {
        if (selectedGunpla) {
            setFormData(selectedGunpla);
        } else {
            setFormData(initialFormState);
        }
    }, [selectedGunpla]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({ ...prev, [name]: value }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            if (selectedGunpla) {
                await updateGunpla(selectedGunpla.id, formData);
                setSelectedGunpla(null);
            } else {
                await addGunpla(formData);
            }
            setFormData(initialFormState);
        } catch (err) {
            console.error('Form submission error:', err);
        }
    };

    const handleCancel = () => {
        setSelectedGunpla(null);
        setFormData(initialFormState);
    };

    return (
        <div style={{ marginBottom: '2rem' }}>
            <h2>{selectedGunpla ? 'Edit Gunpla' : 'Add New Gunpla'}</h2>
            {error && <ErrorMessage message={error} />}
            <form onSubmit={handleSubmit}>
                {/* ...inputs for name, series, grade, scale... */}
                <button type="submit" style={{ marginRight: '1rem' }}>
                    {selectedGunpla ? 'Update' : 'Add'}
                </button>
                {selectedGunpla && (
                    <button type="button" onClick={handleCancel}>
                        Cancel
                    </button>
                )}
            </form>
        </div>
    );
}

export default GunplaForm;
```

- This form either **adds** a new Gunpla or **updates** an existing one.
- We use the context to call `addGunpla` or `updateGunpla`.
- Notice how we store input values in **state** (`formData`) and respond to **events** (`onSubmit`, `onChange`).

#### `GunplaList.jsx` & `GunplaItem.jsx`

**`GunplaList.jsx`:**

```jsx
import React, { useContext } from 'react';
import { GunplaContext } from '../../context/GunplaContext';
import GunplaItem from './GunplaItem';
import LoadingSpinner from '../common/LoadingSpinner';
import ErrorMessage from '../common/ErrorMessage';

function GunplaList() {
    const { gunplas, loading, error } = useContext(GunplaContext);

    if (loading) return <LoadingSpinner />;
    if (error) return <ErrorMessage message={error} />;

    return (
        <div>
            <h2>Gunpla Models List</h2>
            {gunplas.length === 0 ? (
                <p>No gunpla models found</p>
            ) : (
                <ul style={{ listStyleType: 'none', padding: 0 }}>
                    {gunplas.map(gunpla => (
                        <GunplaItem key={gunpla.id} gunpla={gunpla} />
                    ))}
                </ul>
            )}
        </div>
    );
}

export default GunplaList;
```

**`GunplaItem.jsx`:**

```jsx
import React, { useContext } from 'react';
import { GunplaContext } from '../../context/GunplaContext';

function GunplaItem({ gunpla }) {
    const { deleteGunpla, setSelectedGunpla } = useContext(GunplaContext);

    const handleDelete = async () => {
        if (window.confirm('Are you sure you want to delete this Gunpla model?')) {
            try {
                await deleteGunpla(gunpla.id);
            } catch (err) {
                console.error('Delete error:', err);
            }
        }
    };

    return (
        <li style={{
            border: '1px solid #ccc',
            padding: '1rem',
            marginBottom: '1rem',
            borderRadius: '4px'
        }}>
            <h3>{gunpla.name}</h3>
            <p><strong>Series:</strong> {gunpla.series}</p>
            <p><strong>Grade:</strong> {gunpla.grade}</p>
            <p><strong>Scale:</strong> {gunpla.scale}</p>
            <button 
                onClick={() => setSelectedGunpla(gunpla)} 
                style={{ marginRight: '1rem' }}
            >
                Edit
            </button>
            <button 
                onClick={handleDelete}
                style={{ backgroundColor: '#ff4444', color: 'white' }}
            >
                Delete
            </button>
        </li>
    );
}

export default GunplaItem;
```

- The list fetches data (from context) and displays it using a child `GunplaItem` component.
- Each `GunplaItem` includes **Edit** and **Delete** buttons, calling context methods.
- This is an example of how components can be broken down further (List -> Items).

#### `gunplaApi.js`

```js
const API_URL = import.meta.env.VITE_API_URL || '';

export const fetchGunplas = async () => {
    const response = await fetch(`${API_URL}/gunplas`);
    if (!response.ok) {
        throw new Error('Failed to fetch gunplas');
    }
    return response.json();
};

// ...createGunpla, updateGunpla, deleteGunpla omitted for brevity...
```

- Manages all the API requests (like a Python **service** or **model** query).
- We use `fetch` to talk to the backend endpoints (or mock servers in tests).
- Notice how we handle **errors** by throwing an exception that is caught in the context.

#### `setupTests.js`, `testUtils.jsx`

- These files are about testing setup using [Vitest](https://vitest.dev/) and [React Testing Library](https://testing-library.com/).
- `setupTests.js` sets up a **mock service worker (MSW)** to intercept API calls.
- `testUtils.jsx` provides a custom render function that **wraps** your components in the `GunplaProvider` for tests.

For now, just know they ensure our test environment is ready to handle fetch calls and context.

---

## Running the App

1. **Install dependencies**:

   ```bash
   cd frontend
   npm install
   ```

2. **Start the dev server**:

   ```bash
   npm run dev
   ```

3. Open your browser at the address shown in your terminal (usually `http://127.0.0.1:5173` or something similar).

You should see the Gunpla Manager interface. Try adding a new Gunpla model, editing an existing one, or deleting one.

---

## Testing

To run the tests:

```bash
npm test
```

Or to run tests with coverage:

```bash
npm run test:coverage
```

This uses **Vitest** (similar to how Python might use `pytest`). The mock server (MSW) is used to simulate API responses, making tests straightforward without having to spin up a real backend.

---

That’s the overview! As a Python developer, you can see how React’s components and context are conceptually similar to passing data around with function arguments or Django context dictionaries. However, React re-renders components when **state** changes, so you don’t need to manually worry about generating new HTML or reloading the page. Instead, the React engine automatically updates the DOM based on changes to **state** or **props**.

Feel free to explore the components, tweak them, and see how changes in state reflect immediately on the screen!

