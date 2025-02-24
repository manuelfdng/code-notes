// src/components/gunpla/__tests__/GunplaItem.test.jsx
import React from 'react';
import { render, screen } from '../../../test-utils';
import userEvent from '@testing-library/user-event';
import GunplaItem from '../GunplaItem';
import { GunplaContext } from '../../../context/GunplaContext';
import { describe, it, expect, vi, beforeEach } from 'vitest';

const mockGunpla = {
  id: 1,
  name: "RX-78-2 Gundam",
  series: "Mobile Suit Gundam",
  grade: "Master Grade",
  scale: "1/100"
};

describe('GunplaItem', () => {
  const mockContextValue = {
    deleteGunpla: vi.fn(),
    setSelectedGunpla: vi.fn()
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('renders gunpla details', () => {
    render(
      <GunplaContext.Provider value={mockContextValue}>
        <GunplaItem gunpla={mockGunpla} />
      </GunplaContext.Provider>
    );
    
    expect(screen.getByText(mockGunpla.name)).toBeInTheDocument();
    expect(screen.getByText(new RegExp(mockGunpla.series))).toBeInTheDocument();
    expect(screen.getByText(new RegExp(mockGunpla.grade))).toBeInTheDocument();
    expect(screen.getByText(new RegExp(mockGunpla.scale))).toBeInTheDocument();
  });

  it('calls setSelectedGunpla when edit button is clicked', async () => {
    const user = userEvent.setup();
    
    render(
      <GunplaContext.Provider value={mockContextValue}>
        <GunplaItem gunpla={mockGunpla} />
      </GunplaContext.Provider>
    );

    await user.click(screen.getByRole('button', { name: /edit/i }));
    expect(mockContextValue.setSelectedGunpla).toHaveBeenCalledWith(mockGunpla);
  });

  it('calls deleteGunpla when delete is confirmed', async () => {
    const user = userEvent.setup();
    vi.spyOn(window, 'confirm').mockImplementation(() => true);

    render(
      <GunplaContext.Provider value={mockContextValue}>
        <GunplaItem gunpla={mockGunpla} />
      </GunplaContext.Provider>
    );

    await user.click(screen.getByRole('button', { name: /delete/i }));
    expect(mockContextValue.deleteGunpla).toHaveBeenCalledWith(mockGunpla.id);
  });

  it('does not call deleteGunpla when delete is cancelled', async () => {
    const user = userEvent.setup();
    vi.spyOn(window, 'confirm').mockImplementation(() => false);

    render(
      <GunplaContext.Provider value={mockContextValue}>
        <GunplaItem gunpla={mockGunpla} />
      </GunplaContext.Provider>
    );

    await user.click(screen.getByRole('button', { name: /delete/i }));
    expect(mockContextValue.deleteGunpla).not.toHaveBeenCalled();
  });
});