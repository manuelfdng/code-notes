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
    const [loading, setLoading] = useState(false);
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