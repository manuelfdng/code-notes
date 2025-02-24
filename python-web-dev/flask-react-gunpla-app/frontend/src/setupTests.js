// src/setupTests.js
import '@testing-library/jest-dom';
import { afterAll, afterEach, beforeAll } from 'vitest';
import { setupServer } from 'msw/node';
import { rest } from 'msw';

// -----------------------------------------------------------------
// IMPORTANT:
//   - Remove any old import { http, HttpResponse } from 'msw'
//   - Use rest and ctx like below
// -----------------------------------------------------------------

// Define your default (global) mock handlers here:
export const handlers = [
  // GET /gunplas
  rest.get('/gunplas', (req, res, ctx) => {
    return res(
      ctx.status(200),
      ctx.json([
        {
          id: 1,
          name: "RX-78-2 Gundam",
          series: "Mobile Suit Gundam",
          grade: "Master Grade",
          scale: "1/100"
        }
      ])
    );
  }),

  // POST /gunplas
  rest.post('/gunplas', async (req, res, ctx) => {
    const body = await req.json();
    return res(
      ctx.status(201),
      ctx.json({ id: 2, ...body })
    );
  }),

  // PUT /gunplas/:id
  rest.put('/gunplas/:id', async (req, res, ctx) => {
    const { id } = req.params;
    const body = await req.json();
    return res(
      ctx.status(200),
      ctx.json({ id: Number(id), ...body })
    );
  }),

  // DELETE /gunplas/:id
  rest.delete('/gunplas/:id', (req, res, ctx) => {
    return res(
      ctx.status(200),
      ctx.json({ message: 'Gunpla model deleted successfully' })
    );
  }),
];

const server = setupServer(...handlers);

// Start the server before all tests
beforeAll(() => server.listen({ onUnhandledRequest: 'error' }));

// Reset any runtime handlers tests may use
afterEach(() => server.resetHandlers());

// Clean up after the tests are finished
afterAll(() => server.close());
