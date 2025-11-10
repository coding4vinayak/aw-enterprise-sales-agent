import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    host: '0.0.0.0',
    open: false, // Don't auto-open in development
    // Enable HMR for better development experience
    hmr: {
      overlay: true,
    },
  },
  define: {
    global: 'globalThis',
  },
  // Handle client-side routing, fallback to index.html
  appType: 'spa',
  // Explicitly set the root directory
  root: '.',
  // Explicitly set the index.html entry point
  build: {
    outDir: 'dist',
    emptyOutDir: true,
  }
})