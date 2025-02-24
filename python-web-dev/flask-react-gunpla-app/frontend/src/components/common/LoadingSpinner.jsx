import React from 'react';

function LoadingSpinner() {
    return (
        <div style={{ 
            display: 'flex', 
            justifyContent: 'center', 
            padding: '2rem' 
        }}>
            <div>Loading...</div>
        </div>
    );
}

export default LoadingSpinner;
