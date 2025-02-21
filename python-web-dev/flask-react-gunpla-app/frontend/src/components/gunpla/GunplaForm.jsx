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
                <div>
                    <label>Name:</label><br />
                    <input
                        type="text"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Series:</label><br />
                    <input
                        type="text"
                        name="series"
                        value={formData.series}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Grade:</label><br />
                    <input
                        type="text"
                        name="grade"
                        value={formData.grade}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Scale:</label><br />
                    <input
                        type="text"
                        name="scale"
                        value={formData.scale}
                        onChange={handleChange}
                    />
                </div>
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