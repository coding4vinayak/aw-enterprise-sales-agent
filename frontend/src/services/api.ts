import axios, { AxiosInstance } from 'axios';

// Get API base URL from environment
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

// Create axios instance
const api: AxiosInstance = axios.create({
  baseURL: `${API_BASE_URL}/api/v1`,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor to add auth token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('es_agent_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor to handle token refresh
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;
    
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      
      // Try to refresh token
      const refreshToken = localStorage.getItem('es_agent_refresh_token');
      if (refreshToken) {
        try {
          // Implement token refresh logic here
          // For now, just redirect to login
          localStorage.removeItem('es_agent_token');
          localStorage.removeItem('es_agent_refresh_token');
          window.location.href = '/login';
        } catch (refreshError) {
          // If refresh fails, redirect to login
          localStorage.removeItem('es_agent_token');
          localStorage.removeItem('es_agent_refresh_token');
          window.location.href = '/login';
        }
      } else {
        // No refresh token, redirect to login
        window.location.href = '/login';
      }
    }
    
    return Promise.reject(error);
  }
);

export { api };