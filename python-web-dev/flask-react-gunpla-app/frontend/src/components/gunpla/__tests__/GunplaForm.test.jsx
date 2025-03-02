// src/components/gunpla/__tests__/GunplaForm.test.jsx
import React from 'react';
import { render, screen, waitFor } from '../../../testUtils';
import userEvent from '@testing-library/user-event';
import GunplaForm from '../GunplaForm';
import { GunplaContext } from '../../../context/GunplaContext';
import { describe, it, expect, vi, beforeEach } from 'vitest';

describe('GunplaForm', () => {
  const mockContextValue = {
    addGunpla: vi.fn(),
    updateGunpla: vi.fn(),
    selectedGunpla: null,
    setSelectedGunpla: vi.fn(),
    error: null
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('renders empty form initially', () => {
    render(
      <GunplaContext.Provider value={mockContextValue}>
        <GunplaForm />
      </GunplaContext.Provider>
    );
    
    expect(screen.getByLabelText(/name/i)).toHaveValue('');
    expect(screen.getByLabelText(/series/i)).toHaveValue('');
    expect(screen.getByLabelText(/grade/i)).toHaveValue('');
    expect(screen.getByLabelText(/scale/i)).toHaveValue('');
  });

  it('updates form fields when typing', async () => {
    const user = userEvent.setup();
    
    render(
      <GunplaContext.Provider value={mockContextValue}>
        <GunplaForm />
      </GunplaContext.Provider>
    );
    
    const nameInput = screen.getByLabelText(/name/i);
    await user.type(nameInput, 'Test Gundam');
    expect(nameInput).toHaveValue('Test Gundam');
  });

  it('submits form with correct data', async () => {
    const user = userEvent.setup();
    
    render(
      <GunplaContext.Provider value={mockContextValue}>
        <GunplaForm />
      </GunplaContext.Provider>
    );

    await user.type(screen.getByLabelText(/name/i), 'Test Gundam');
    await user.type(screen.getByLabelText(/series/i), 'Test Series');
    await user.type(screen.getByLabelText(/grade/i), 'Test Grade');
    await user.type(screen.getByLabelText(/scale/i), '1/144');

    await user.click(screen.getByRole('button', { name: /add/i }));

    expect(mockContextValue.addGunpla).toHaveBeenCalledWith({
      name: 'Test Gundam',
      series: 'Test Series',
      grade: 'Test Grade',
      scale: '1/144'
    });
  });

  it('handles edit mode correctly', async () => {
    const user = userEvent.setup();
    const editContextValue = {
      ...mockContextValue,
      selectedGunpla: {
        id: 1,
        name: 'Edit Gundam',
        series: 'Edit Series',
        grade: 'Edit Grade',
        scale: '1/100'
      }
    };

    render(
      <GunplaContext.Provider value={editContextValue}>
        <GunplaForm />
      </GunplaContext.Provider>
    );

    expect(screen.getByLabelText(/name/i)).toHaveValue('Edit Gundam');
    expect(screen.getByRole('button', { name: /update/i })).toBeInTheDocument();

    await user.clear(screen.getByLabelText(/name/i));
    await user.type(screen.getByLabelText(/name/i), 'Updated Gundam');
    await user.click(screen.getByRole('button', { name: /update/i }));

    expect(mockContextValue.updateGunpla).toHaveBeenCalledWith(1, {
      id: 1,
      name: 'Updated Gundam',
      series: 'Edit Series',
      grade: 'Edit Grade',
      scale: '1/100'
    });
  });
});