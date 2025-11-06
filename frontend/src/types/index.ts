// User Types
export interface User {
  id: string;
  email: string;
  name: string;
  role: 'owner' | 'admin' | 'user' | 'viewer';
  tenant_id: string;
  is_active: boolean;
  is_verified: boolean;
  last_login_at?: string;
  created_at: string;
  updated_at: string;
}

// Lead Types
export interface Lead {
  id: string;
  tenant_id: string;
  user_id: string;
  email?: string;
  name?: string;
  company?: string;
  domain?: string;
  title?: string;
  linkedin_url?: string;
  phone?: string;
  status: string;
  source: string;
  enriched_data?: Record<string, any>;
  crm_contact_id?: string;
  crm_account_id?: string;
  created_at: string;
  updated_at: string;
}

// Agent Execution Types
export interface AgentExecution {
  id: string;
  tenant_id: string;
  user_id: string;
  lead_id: string;
  agent_type: string;
  trajectory: string;
  success: boolean;
  tokens_input: number;
  tokens_output: number;
  cost_cents: number;
  started_at: string;
  completed_at: string;
  created_at: string;
  updated_at: string;
}

// Campaign Types
export interface Campaign {
  id: string;
  name: string;
  description?: string;
  status: 'draft' | 'active' | 'paused' | 'completed';
  created_at: string;
  updated_at: string;
  active_leads: number;
  completed_leads: number;
}

// Tenant Types
export interface Tenant {
  id: string;
  name: string;
  subdomain: string;
  plan: string;
  status: string;
  config?: Record<string, any>;
  limits?: Record<string, any>;
  billing_email?: string;
  is_verified: boolean;
  created_at: string;
  updated_at: string;
}

// Usage Metrics Types
export interface UsageMetrics {
  id: string;
  tenant_id: string;
  user_id?: string;
  date: string;
  metric_type: string;
  value: number;
  cost_cents: number;
  created_at: string;
}

// Auth Types
export interface LoginCredentials {
  email: string;
  password: string;
}

export interface RegisterCredentials {
  name: string;
  email: string;
  password: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
}

// Common Types
export interface ApiResponse<T> {
  data: T;
  message?: string;
  success: boolean;
}