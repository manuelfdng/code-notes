// frontend/vite.config.js
import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig(({ mode }) => {  
  const target = `http://127.0.0.1:5000`;

  return {
    plugins: [react()],
    server: {
      proxy: {
        '/gunplas': {
          target,
          changeOrigin: true,
          secure: false, // set to false if using self-signed certs
        },
      },
    },
  };
});