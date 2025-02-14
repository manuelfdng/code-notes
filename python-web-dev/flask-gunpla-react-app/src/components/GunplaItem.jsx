import React, { useContext } from 'react';
import { GunplaContext } from '../context/GunplaContext';

function GunplaItem({ gunpla }) {
  const { deleteGunpla, setSelectedGunpla } = useContext(GunplaContext);

  return (
    <li style={{
      border: '1px solid #ccc',
      padding: '1rem',
      marginBottom: '1rem'
    }}>
      <h3>{gunpla.name}</h3>
      <p><strong>Series:</strong> {gunpla.series}</p>
      <p><strong>Grade:</strong> {gunpla.grade}</p>
      <p><strong>Scale:</strong> {gunpla.scale}</p>
      <button onClick={() => setSelectedGunpla(gunpla)} style={{ marginRight: '1rem' }}>
        Edit
      </button>
      <button onClick={() => deleteGunpla(gunpla.id)}>
        Delete
      </button>
    </li>
  );
}

export default GunplaItem;