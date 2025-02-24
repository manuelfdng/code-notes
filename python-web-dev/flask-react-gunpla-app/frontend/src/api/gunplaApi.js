const API_URL = import.meta.env.VITE_API_URL || '';

export const fetchGunplas = async () => {
    const response = await fetch(`${API_URL}/gunplas`);
    if (!response.ok) {
        throw new Error('Failed to fetch gunplas');
    }
    return response.json();
};

export const createGunpla = async (gunpla) => {
    const response = await fetch(`${API_URL}/gunplas`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(gunpla)
    });
    if (!response.ok) {
        throw new Error('Failed to add gunpla');
    }
    return response.json();
};

export const updateGunpla = async (id, gunpla) => {
    const response = await fetch(`${API_URL}/gunplas/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(gunpla)
    });
    if (!response.ok) {
        throw new Error('Failed to update gunpla');
    }
    return response.json();
};

export const deleteGunpla = async (id) => {
    const response = await fetch(`${API_URL}/gunplas/${id}`, {
        method: 'DELETE'
    });
    if (!response.ok) {
        throw new Error('Failed to delete gunpla');
    }
    return response.json();
};
