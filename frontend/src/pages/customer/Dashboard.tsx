import React from 'react';
import { useQuery } from '@tanstack/react-query';
import { 
  UserGroupIcon, 
  ChatBubbleLeftRightIcon, 
  CalendarIcon, 
  ChartBarIcon,
  Cog6ToothIcon
} from '@heroicons/react/24/outline';
import { api } from '../../services/api';
import { Lead, AgentExecution } from '../../types';

const CustomerDashboard: React.FC = () => {
  // Fetch dashboard metrics
  const { data: metrics, isLoading: isMetricsLoading } = useQuery({
    queryKey: ['dashboard-metrics'],
    queryFn: async () => {
      // Mock data for demo
      return {
        totalLeads: 243,
        meetingsBooked: 18,
        responseRate: 32,
        pipelineValue: 124000
      };
    },
    staleTime: 5 * 60 * 1000, // 5 minutes
  });

  // Fetch recent leads
  const { data: leads, isLoading: isLeadsLoading } = useQuery({
    queryKey: ['recent-leads'],
    queryFn: async () => {
      // This would be an API call in a real app
      const mockLeads: Lead[] = [
        { id: '1', name: 'John Smith', company: 'Acme Corp', status: 'contacted', created_at: '2023-05-15T10:30:00Z', updated_at: '2023-05-15T10:30:00Z', tenant_id: '1', user_id: '1', source: 'agent' },
        { id: '2', name: 'Sarah Johnson', company: 'Tech Solutions', status: 'new', created_at: '2023-05-16T14:20:00Z', updated_at: '2023-05-16T14:20:00Z', tenant_id: '1', user_id: '1', source: 'agent' },
        { id: '3', name: 'Mike Williams', company: 'Global Inc', status: 'qualified', created_at: '2023-05-17T09:15:00Z', updated_at: '2023-05-17T09:15:00Z', tenant_id: '1', user_id: '1', source: 'agent' },
      ];
      return mockLeads;
    },
    staleTime: 2 * 60 * 1000, // 2 minutes
  });

  // Fetch recent agent executions
  const { data: agentExecutions, isLoading: isAgentExecutionsLoading } = useQuery({
    queryKey: ['recent-agent-executions'],
    queryFn: async () => {
      // This would be an API call in a real app
      const mockExecutions: AgentExecution[] = [
        { id: '1', lead_id: '1', user_id: '1', tenant_id: '1', agent_type: 'research', success: true, started_at: '2023-05-15T11:00:00Z', completed_at: '2023-05-15T11:02:00Z', created_at: '2023-05-15T11:00:00Z', updated_at: '2023-05-15T11:02:00Z', cost_cents: 15, tokens_input: 120, tokens_output: 80, trajectory: '[]' },
        { id: '2', lead_id: '2', user_id: '1', tenant_id: '1', agent_type: 'research', success: true, started_at: '2023-05-16T15:00:00Z', completed_at: '2023-05-16T15:01:30Z', created_at: '2023-05-16T15:00:00Z', updated_at: '2023-05-16T15:01:30Z', cost_cents: 12, tokens_input: 95, tokens_output: 65, trajectory: '[]' },
      ];
      return mockExecutions;
    },
    staleTime: 2 * 60 * 1000, // 2 minutes
  });

  return (
    <div className="space-y-6">
      {/* Page header */}
      <div className="sm:flex sm:items-center">
        <div className="sm:flex-auto">
          <h1 className="text-xl font-semibold text-gray-900">Dashboard</h1>
          <p className="mt-2 text-sm text-gray-700">
            Welcome back! Here's what's happening with your sales activities.
          </p>
        </div>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
        <div className="bg-white overflow-hidden shadow rounded-lg">
          <div className="px-4 py-5 sm:p-6">
            <div className="flex items-center">
              <div className="flex-shrink-0 bg-indigo-500 rounded-md p-3">
                <UserGroupIcon className="h-6 w-6 text-white" />
              </div>
              <div className="ml-5 w-0 flex-1">
                <dl>
                  <dt className="text-sm font-medium text-gray-500 truncate">Active Leads</dt>
                  <dd className="flex items-baseline">
                    <div className="text-2xl font-semibold text-gray-900">
                      {isMetricsLoading ? '...' : metrics?.totalLeads}
                    </div>
                  </dd>
                </dl>
              </div>
            </div>
          </div>
        </div>

        <div className="bg-white overflow-hidden shadow rounded-lg">
          <div className="px-4 py-5 sm:p-6">
            <div className="flex items-center">
              <div className="flex-shrink-0 bg-green-500 rounded-md p-3">
                <CalendarIcon className="h-6 w-6 text-white" />
              </div>
              <div className="ml-5 w-0 flex-1">
                <dl>
                  <dt className="text-sm font-medium text-gray-500 truncate">Meetings Booked</dt>
                  <dd className="flex items-baseline">
                    <div className="text-2xl font-semibold text-gray-900">
                      {isMetricsLoading ? '...' : metrics?.meetingsBooked}
                    </div>
                  </dd>
                </dl>
              </div>
            </div>
          </div>
        </div>

        <div className="bg-white overflow-hidden shadow rounded-lg">
          <div className="px-4 py-5 sm:p-6">
            <div className="flex items-center">
              <div className="flex-shrink-0 bg-blue-500 rounded-md p-3">
                <ChatBubbleLeftRightIcon className="h-6 w-6 text-white" />
              </div>
              <div className="ml-5 w-0 flex-1">
                <dl>
                  <dt className="text-sm font-medium text-gray-500 truncate">Response Rate</dt>
                  <dd className="flex items-baseline">
                    <div className="text-2xl font-semibold text-gray-900">
                      {isMetricsLoading ? '...' : `${metrics?.responseRate}%`}
                    </div>
                  </dd>
                </dl>
              </div>
            </div>
          </div>
        </div>

        <div className="bg-white overflow-hidden shadow rounded-lg">
          <div className="px-4 py-5 sm:p-6">
            <div className="flex items-center">
              <div className="flex-shrink-0 bg-purple-500 rounded-md p-3">
                <ChartBarIcon className="h-6 w-6 text-white" />
              </div>
              <div className="ml-5 w-0 flex-1">
                <dl>
                  <dt className="text-sm font-medium text-gray-500 truncate">Pipeline Value</dt>
                  <dd className="flex items-baseline">
                    <div className="text-2xl font-semibold text-gray-900">
                      {isMetricsLoading ? '...' : metrics ? `$${(metrics.pipelineValue / 1000).toFixed(0)}K` : ''}
                    </div>
                  </dd>
                </dl>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Recent activity */}
      <div className="grid grid-cols-1 gap-6 lg:grid-cols-2">
        {/* Recent Leads */}
        <div className="bg-white shadow overflow-hidden sm:rounded-lg">
          <div className="px-4 py-5 border-b border-gray-200 sm:px-6">
            <h3 className="text-lg leading-6 font-medium text-gray-900">Recent Leads</h3>
          </div>
          <ul className="divide-y divide-gray-200">
            {isLeadsLoading ? (
              <li className="px-4 py-4 sm:px-6">
                <div className="animate-pulse flex space-x-4">
                  <div className="flex-1 space-y-2 py-1">
                    <div className="h-4 bg-gray-200 rounded w-3/4"></div>
                    <div className="h-4 bg-gray-200 rounded"></div>
                    <div className="h-4 bg-gray-200 rounded w-5/6"></div>
                  </div>
                </div>
              </li>
            ) : (
              leads?.slice(0, 5).map((lead) => (
                <li key={lead.id} className="px-4 py-4 sm:px-6">
                  <div className="flex items-center justify-between">
                    <div className="text-sm font-medium text-indigo-600 truncate">{lead.name}</div>
                    <div className="ml-2 flex-shrink-0 flex">
                      <span className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                        {lead.status}
                      </span>
                    </div>
                  </div>
                  <div className="mt-2 flex justify-between text-sm text-gray-500">
                    <p className="truncate">{lead.company}</p>
                    <p>{new Date(lead.created_at).toLocaleDateString()}</p>
                  </div>
                </li>
              ))
            )}
          </ul>
        </div>

        {/* Recent Agent Executions */}
        <div className="bg-white shadow overflow-hidden sm:rounded-lg">
          <div className="px-4 py-5 border-b border-gray-200 sm:px-6">
            <h3 className="text-lg leading-6 font-medium text-gray-900">Recent Agent Executions</h3>
          </div>
          <ul className="divide-y divide-gray-200">
            {isAgentExecutionsLoading ? (
              <li className="px-4 py-4 sm:px-6">
                <div className="animate-pulse flex space-x-4">
                  <div className="flex-1 space-y-2 py-1">
                    <div className="h-4 bg-gray-200 rounded w-3/4"></div>
                    <div className="h-4 bg-gray-200 rounded"></div>
                    <div className="h-4 bg-gray-200 rounded w-5/6"></div>
                  </div>
                </div>
              </li>
            ) : (
              agentExecutions?.slice(0, 5).map((execution) => (
                <li key={execution.id} className="px-4 py-4 sm:px-6">
                  <div className="flex items-center justify-between">
                    <div className="text-sm font-medium text-indigo-600 truncate">
                      {execution.agent_type} agent
                    </div>
                    <div className="ml-2 flex-shrink-0 flex">
                      <span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${
                        execution.success 
                          ? 'bg-green-100 text-green-800' 
                          : 'bg-red-100 text-red-800'
                      }`}>
                        {execution.success ? 'Success' : 'Failed'}
                      </span>
                    </div>
                  </div>
                  <div className="mt-2 flex justify-between text-sm text-gray-500">
                    <p>${(execution.cost_cents / 100).toFixed(2)}</p>
                    <p>{new Date(execution.started_at).toLocaleString()}</p>
                  </div>
                </li>
              ))
            )}
          </ul>
        </div>
      </div>

      {/* Quick actions */}
      <div className="mt-8">
        <h3 className="text-lg leading-6 font-medium text-gray-900 mb-4">Quick Actions</h3>
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
          <button className="bg-white shadow rounded-lg p-6 text-center hover:shadow-md transition-shadow">
            <div className="mx-auto flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white">
              <UserGroupIcon className="h-6 w-6" />
            </div>
            <h4 className="mt-4 text-sm font-medium text-gray-900">Add Lead</h4>
            <p className="mt-1 text-sm text-gray-500">Add a new lead to your database</p>
          </button>
          
          <button className="bg-white shadow rounded-lg p-6 text-center hover:shadow-md transition-shadow">
            <div className="mx-auto flex items-center justify-center h-12 w-12 rounded-md bg-green-500 text-white">
              <ChatBubbleLeftRightIcon className="h-6 w-6" />
            </div>
            <h4 className="mt-4 text-sm font-medium text-gray-900">Run Agent</h4>
            <p className="mt-1 text-sm text-gray-500">Execute an AI agent on a lead</p>
          </button>
          
          <button className="bg-white shadow rounded-lg p-6 text-center hover:shadow-md transition-shadow">
            <div className="mx-auto flex items-center justify-center h-12 w-12 rounded-md bg-blue-500 text-white">
              <ChartBarIcon className="h-6 w-6" />
            </div>
            <h4 className="mt-4 text-sm font-medium text-gray-900">Create Campaign</h4>
            <p className="mt-1 text-sm text-gray-500">Start a new outreach campaign</p>
          </button>
          
          <button className="bg-white shadow rounded-lg p-6 text-center hover:shadow-md transition-shadow">
            <div className="mx-auto flex items-center justify-center h-12 w-12 rounded-md bg-purple-500 text-white">
              <Cog6ToothIcon className="h-6 w-6" />
            </div>
            <h4 className="mt-4 text-sm font-medium text-gray-900">Sync CRM</h4>
            <p className="mt-1 text-sm text-gray-500">Sync with your CRM system</p>
          </button>
        </div>
      </div>
    </div>
  );
};

export default CustomerDashboard;