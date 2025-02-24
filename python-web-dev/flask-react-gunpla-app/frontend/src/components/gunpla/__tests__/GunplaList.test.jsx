// src/components/gunpla/__tests__/GunplaList.test.jsx
import React from 'react';
import { render, screen } from '../../../test-utils';
import GunplaList from '../GunplaList';
import { GunplaContext } from '../../../context/GunplaContext';
import { describe, it, expect, vi } from 'vitest';

describe('GunplaList', () => {
  it('renders loading state', () => {
    render(
      <GunplaContext.Provider value={{ loading: true, gunplas: [], error: null }}>
        <GunplaList />
      </GunplaContext.Provider>
    );
    
    expect(screen.getByText(/loading/i)).toBeInTheDocument();
  });

  it('renders gunpla list', () => {
    const mockGunplas = [
      {
        id: 1,
        name: "RX-78-2 Gundam",
        series: "Mobile Suit Gundam",
        grade: "Master Grade",
        scale: "1/100"
      }
    ];

    render(
      <GunplaContext.Provider value={{ loading: false, gunplas: mockGunplas, error: null }}>
        <GunplaList />
      </GunplaContext.Provider>
    );

    expect(screen.getByText('RX-78-2 Gundam')).toBeInTheDocument();
    expect(screen.getByText(/mobile suit gundam/i)).toBeInTheDocument();
  });

  it('renders empty state message', () => {
    render(
      <GunplaContext.Provider value={{ loading: false, gunplas: [], error: null }}>
        <GunplaList />
      </GunplaContext.Provider>
    );

    expect(screen.getByText(/no gunpla models found/i)).toBeInTheDocument();
  });

  it('renders error message', () => {
    render(
      <GunplaContext.Provider value={{ 
        loading: false, 
        gunplas: [], 
        error: 'Failed to fetch gunplas' 
      }}>
        <GunplaList />
      </GunplaContext.Provider>
    );

    expect(screen.getByText(/failed to fetch gunplas/i)).toBeInTheDocument();
  });
});
