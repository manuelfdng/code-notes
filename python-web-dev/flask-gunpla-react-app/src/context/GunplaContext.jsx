import React, { createContext, useState, useEffect } from 'react';

export const GunplaContext = createContext();

export const GunplaProvider = ({ children }) => {
  // Use environment variable if available; otherwise, use relative paths (to work with Vite proxy)
  const API_URL = import.meta.env.VITE_API_URL || '';

  const [gunplas, setGunplas] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [selectedGunpla, setSelectedGunpla] = useState(null); // For editing

  const fetchGunplas = async () => {
    setLoading(true);
    try {
      const response = await fetch(`${API_URL}/gunplas`);
      if (!response.ok) {
        throw new Error('Failed to fetch gunplas');
      }
      const data = await response.json();
      setGunplas(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const addGunpla = async (gunpla) => {
    try {
      const response = await fetch(`${API_URL}/gunplas`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(gunpla)
      });
      if (!response.ok) {
        throw new Error('Failed to add gunpla');
      }
      const data = await response.json();
      setGunplas(prev => [...prev, data]);
    } catch (err) {
      setError(err.message);
    }
  };

  const updateGunpla = async (id, updatedGunpla) => {
    try {
      const response = await fetch(`${API_URL}/gunplas/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(updatedGunpla)
      });
      if (!response.ok) {
        throw new Error('Failed to update gunpla');
      }
      const data = await response.json();
      setGunplas(prev => prev.map(g => (g.id === id ? data : g)));
    } catch (err) {
      setError(err.message);
    }
  };

  const deleteGunpla = async (id) => {
    try {
      const response = await fetch(`${API_URL}/gunplas/${id}`, {
        method: 'DELETE'
      });
      if (!response.ok) {
        throw new Error('Failed to delete gunpla');
      }
      setGunplas(prev => prev.filter(g => g.id !== id));
    } catch (err) {
      setError(err.message);
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