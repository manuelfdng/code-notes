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
