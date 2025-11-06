import { api } from './api';
import { Campaign } from '../types';

// Campaign-related API calls
export const campaignService = {
  // Get campaigns
  getCampaigns: async (params?: { skip?: number; limit?: number }) => {
    const response = await api.get('/customer/campaigns', { params });
    return response.data as Campaign[];
  },

  // Get campaign by ID
  getCampaign: async (campaignId: string) => {
    const response = await api.get(`/customer/campaigns/${campaignId}`);
    return response.data as Campaign;
  },

  // Create campaign
  createCampaign: async (campaignData: Partial<Campaign>) => {
    const response = await api.post('/customer/campaigns', campaignData);
    return response.data as Campaign;
  },

  // Update campaign
  updateCampaign: async (campaignId: string, campaignData: Partial<Campaign>) => {
    const response = await api.put(`/customer/campaigns/${campaignId}`, campaignData);
    return response.data as Campaign;
  },

  // Delete campaign
  deleteCampaign: async (campaignId: string) => {
    const response = await api.delete(`/customer/campaigns/${campaignId}`);
    return response.data;
  },

  // Activate campaign
  activateCampaign: async (campaignId: string) => {
    const response = await api.post(`/customer/campaigns/${campaignId}/activate`);
    return response.data;
  },

  // Deactivate campaign
  deactivateCampaign: async (campaignId: string) => {
    const response = await api.post(`/customer/campaigns/${campaignId}/deactivate`);
    return response.data;
  },

  // Add leads to campaign
  addLeadsToCampaign: async (campaignId: string, leadIds: string[]) => {
    const response = await api.post(`/customer/campaigns/${campaignId}/add-leads`, { lead_ids: leadIds });
    return response.data;
  }
};