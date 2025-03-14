import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { GunplaProvider } from './context/GunplaContext';
import './styles/index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <GunplaProvider>
      <App />
    </GunplaProvider>
  </React.StrictMode>
);
