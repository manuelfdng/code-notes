import React, { useContext } from 'react';
import { GunplaContext } from '../context/GunplaContext';
import GunplaItem from './GunplaItem';

function GunplaList() {
  const { gunplas, loading, error } = useContext(GunplaContext);

  if (loading) return <p>Loading gunpla models...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h2>Gunpla Models List</h2>
      {gunplas.length === 0 ? (
        <p>No gunpla models found.</p>
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