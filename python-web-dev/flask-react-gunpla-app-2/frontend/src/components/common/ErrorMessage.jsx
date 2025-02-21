import React from 'react';

function ErrorMessage({ message }) {
    return (
        <div style={{
            color: 'red',
            padding: '1rem',
            border: '1px solid red',
            borderRadius: '4px',
            margin: '1rem 0'
        }}>
            {message}
        </div>
    );
}

export default ErrorMessage;