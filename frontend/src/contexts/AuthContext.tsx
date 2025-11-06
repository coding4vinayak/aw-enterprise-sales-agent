import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { api } from '../services/api';
import { User } from '../types';

interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
  register: (name: string, email: string, password: string) => Promise<void>;
  checkAuthStatus: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    checkAuthStatus();
  }, []);

  const checkAuthStatus = async () => {
    try {
      const token = localStorage.getItem('es_agent_token');
      if (token) {
        // Verify token and get user info
        const response = await api.get('/auth/me');
        setUser(response.data);
      }
    } catch (error) {
      // Token is invalid or expired
      localStorage.removeItem('es_agent_token');
      localStorage.removeItem('es_agent_refresh_token');
    } finally {
      setLoading(false);
    }
  };

  const login = async (email: string, password: string) => {
    try {
      const response = await api.post('/auth/token', {
        username: email,
        password,
      });
      
      const { access_token } = response.data;
      localStorage.setItem('es_agent_token', access_token);
      
      // Get user info after login
      const userResponse = await api.get('/auth/me');
      setUser(userResponse.data);
    } catch (error) {
      throw new Error('Invalid credentials');
    }
  };

  const logout = () => {
    localStorage.removeItem('es_agent_token');
    localStorage.removeItem('es_agent_refresh_token');
    setUser(null);
  };

  const register = async (name: string, email: string, password: string) => {
    try {
      const response = await api.post('/auth/register', {
        name,
        email,
        password,
      });
      
      // Auto-login after registration
      await login(email, password);
    } catch (error) {
      throw new Error('Registration failed');
    }
  };

  const value = {
    user,
    loading,
    login,
    logout,
    register,
    checkAuthStatus,
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};