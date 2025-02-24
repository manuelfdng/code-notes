// frontend/src/test-utils.jsx
import React from 'react';
import { render } from '@testing-library/react';
import { GunplaProvider } from './context/GunplaContext';

const AllTheProviders = ({ children }) => {
  return (
    <GunplaProvider>
      {children}
    </GunplaProvider>
  );
};

const customRender = (ui, options) =>
  render(ui, { wrapper: AllTheProviders, ...options });

// re-export everything
export * from '@testing-library/react';

// override render method
export { customRender as render };