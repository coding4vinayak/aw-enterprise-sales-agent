import { api } from './api';
import { Lead, AgentExecution, Campaign } from '../types';

// Agent-related API calls
export const agentService = {
  // Execute agent for a lead
  executeAgent: async (leadId: string, agentType: string = 'research') => {
    const response = await api.post(`/customer/agent/execute/${leadId}`, {
      agent_type: agentType
    });
    return response.data;
  },

  // Get agent executions
  getAgentExecutions: async (params?: { skip?: number; limit?: number }) => {
    const response = await api.get('/customer/agent/executions', { params });
    return response.data.executions as AgentExecution[];
  },

  // CRM sync
  syncLeadToCrm: async (leadId: string) => {
    const response = await api.post(`/customer/crm/sync/${leadId}`);
    return response.data;
  },

  createCrmNote: async (leadId: string, content: string) => {
    const response = await api.post(`/customer/crm/note/${leadId}`, { content });
    return response.data;
  }
};