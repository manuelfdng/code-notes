import React, { useContext } from 'react';
import { GunplaContext } from '../../context/GunplaContext';
import GunplaItem from './GunplaItem';
import LoadingSpinner from '../common/LoadingSpinner';
import ErrorMessage from '../common/ErrorMessage';

function GunplaList() {
    const { gunplas, loading, error } = useContext(GunplaContext);

    if (loading) {
        return <LoadingSpinner />;
    }

    if (error) {
        return <ErrorMessage message={error} />;
    }

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
