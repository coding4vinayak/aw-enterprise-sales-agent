import React, { useState } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { 
  PlayIcon, 
  ArrowsRightLeftIcon, 
  MagnifyingGlassIcon,
  DocumentTextIcon,
  Cog6ToothIcon,
  ArrowPathIcon
} from '@heroicons/react/24/outline';
import { api } from '../../services/api';
import { Lead, AgentExecution } from '../../types';

const AgentPage: React.FC = () => {
  const [selectedLead, setSelectedLead] = useState<Lead | null>(null);
  const [agentType, setAgentType] = useState('research');
  const [isExecuting, setIsExecuting] = useState(false);
  const [executionProgress, setExecutionProgress] = useState<number | null>(null);
  const queryClient = useQueryClient();

  // Fetch leads
  const { data: leads, isLoading: leadsLoading } = useQuery({
    queryKey: ['leads'],
    queryFn: async () => {
      // Mock data for demo
      return [
        { id: '1', name: 'John Smith', email: 'john@acmecorp.com', company: 'Acme Corp', status: 'contacted', created_at: '2023-05-15T10:30:00Z', updated_at: '2023-05-15T10:30:00Z', tenant_id: '1', user_id: '1', source: 'agent' },
        { id: '2', name: 'Sarah Johnson', email: 'sarah@techsolutions.com', company: 'Tech Solutions', status: 'new', created_at: '2023-05-16T14:20:00Z', updated_at: '2023-05-16T14:20:00Z', tenant_id: '1', user_id: '1', source: 'agent' },
        { id: '3', name: 'Mike Williams', email: 'mike@globalinc.com', company: 'Global Inc', status: 'qualified', created_at: '2023-05-17T09:15:00Z', updated_at: '2023-05-17T09:15:00Z', tenant_id: '1', user_id: '1', source: 'agent' },
      ];
    }
  });

  // Fetch recent agent executions
  const { data: executions, isLoading: executionsLoading } = useQuery({
    queryKey: ['agent-executions'],
    queryFn: async () => {
      // Mock data for demo
      return [
        { id: '1', lead_id: '1', agent_type: 'research', success: true, started_at: '2023-05-15T11:00:00Z', completed_at: '2023-05-15T11:02:00Z', created_at: '2023-05-15T11:00:00Z', updated_at: '2023-05-15T11:02:00Z', cost_cents: 15, tokens_input: 120, tokens_output: 80 },
        { id: '2', lead_id: '2', agent_type: 'outreach', success: true, started_at: '2023-05-16T15:00:00Z', completed_at: '2023-05-16T15:01:30Z', created_at: '2023-05-16T15:00:00Z', updated_at: '2023-05-16T15:01:30Z', cost_cents: 12, tokens_input: 95, tokens_output: 65 },
      ];
    }
  });

  // Mutation for executing agent
  const executeAgentMutation = useMutation({
    mutationFn: async ({ leadId, type }: { leadId: string; type: string }) => {
      // Simulate API call
      setIsExecuting(true);
      setExecutionProgress(10);
      
      // Simulate steps
      for (let i = 0; i < 5; i++) {
        await new Promise(resolve => setTimeout(resolve, 1000));
        setExecutionProgress(20 + i * 20);
      }
      
      // Mock response
      const mockResult = {
        success: true,
        draft_email: 'Dear John,\n\nI noticed your company is doing interesting work in the tech space. I think our AI-powered sales agent platform could help you increase your lead conversion rate by 25%.\n\nWould you be available for a brief 15-minute demo next week?\n\nBest regards,\nSales Agent',
        research_results: { company_info: { name: 'Acme Corp', industry: 'Technology', size: '200-500' } },
        enriched_data: { linkedin_url: 'https://linkedin.com/company/acmecorp' },
        execution_time: 5.2,
        tokens_used: 245,
        cost_cents: 15
      };
      
      setIsExecuting(false);
      setExecutionProgress(null);
      return mockResult;
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['agent-executions'] });
    },
  });

  const handleExecuteAgent = () => {
    if (!selectedLead) {
      alert('Please select a lead');
      return;
    }
    
    executeAgentMutation.mutate({ leadId: selectedLead.id, type: agentType });
  };

  const getStatusColor = (status: boolean) => {
    return status ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800';
  };

  return (
    <div className="space-y-6">
      {/* Page header */}
      <div className="sm:flex sm:items-center">
        <div className="sm:flex-auto">
          <h1 className="text-xl font-semibold text-gray-900">AI Agent</h1>
          <p className="mt-2 text-sm text-gray-700">
            Execute automated sales agents to research leads and generate outreach
          </p>
        </div>
      </div>

      {/* Main content */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Controls panel */}
        <div className="lg:col-span-1">
          <div className="bg-white shadow rounded-lg p-6">
            <h2 className="text-lg font-medium text-gray-900 mb-4">Agent Configuration</h2>
            
            <div className="space-y-4">
              {/* Lead selection */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Select Lead
                </label>
                <div className="relative">
                  <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <MagnifyingGlassIcon className="h-5 w-5 text-gray-400" aria-hidden="true" />
                  </div>
                  <select
                    className="block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-md leading-5 bg-white placeholder-gray-500 focus:outline-none focus:placeholder-gray-400 focus:ring-1 focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    value={selectedLead?.id || ''}
                    onChange={(e) => {
                      const lead = leads?.find(l => l.id === e.target.value) || null;
                      setSelectedLead(lead);
                    }}
                  >
                    <option value="">Select a lead...</option>
                    {leads?.map(lead => (
                      <option key={lead.id} value={lead.id}>
                        {lead.name} - {lead.company}
                      </option>
                    ))}
                  </select>
                </div>
              </div>

              {/* Agent type selection */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Agent Type
                </label>
                <div className="grid grid-cols-2 gap-3">
                  <button
                    type="button"
                    className={`px-4 py-2 border rounded-md text-sm font-medium ${
                      agentType === 'research'
                        ? 'bg-indigo-100 border-indigo-500 text-indigo-700'
                        : 'border-gray-300 text-gray-700 hover:bg-gray-50'
                    }`}
                    onClick={() => setAgentType('research')}
                  >
                    Research
                  </button>
                  <button
                    type="button"
                    className={`px-4 py-2 border rounded-md text-sm font-medium ${
                      agentType === 'outreach'
                        ? 'bg-indigo-100 border-indigo-500 text-indigo-700'
                        : 'border-gray-300 text-gray-700 hover:bg-gray-50'
                    }`}
                    onClick={() => setAgentType('outreach')}
                  >
                    Outreach
                  </button>
                </div>
              </div>

              {/* Execute button */}
              <button
                type="button"
                disabled={!selectedLead || isExecuting}
                onClick={handleExecuteAgent}
                className="w-full flex justify-center items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50"
              >
                {isExecuting ? (
                  <>
                    <ArrowPathIcon className="animate-spin -ml-1 mr-2 h-4 w-4" />
                    Executing...
                  </>
                ) : (
                  <>
                    <PlayIcon className="-ml-1 mr-2 h-5 w-5" aria-hidden="true" />
                    Execute Agent
                  </>
                )}
              </button>

              {/* Progress bar */}
              {executionProgress !== null && (
                <div className="pt-4">
                  <div className="flex justify-between text-sm text-gray-600 mb-1">
                    <span>Progress</span>
                    <span>{executionProgress}%</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div 
                      className="bg-indigo-600 h-2 rounded-full transition-all duration-300 ease-out" 
                      style={{ width: `${executionProgress}%` }}
                    ></div>
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Agent status panel */}
          <div className="bg-white shadow rounded-lg p-6 mt-6">
            <h2 className="text-lg font-medium text-gray-900 mb-4">Agent Status</h2>
            <div className="space-y-3">
              <div className="flex justify-between">
                <span className="text-sm text-gray-600">Status:</span>
                <span className="text-sm font-medium">
                  {isExecuting ? 'Running' : 'Idle'}
                </span>
              </div>
              <div className="flex justify-between">
                <span className="text-sm text-gray-600">Current Task:</span>
                <span className="text-sm font-medium">
                  {isExecuting ? 'Web Research' : 'Waiting'}
                </span>
              </div>
              <div className="flex justify-between">
                <span className="text-sm text-gray-600">Last Execution:</span>
                <span className="text-sm font-medium">
                  {executions?.[0] ? new Date(executions[0].completed_at).toLocaleString() : 'Never'}
                </span>
              </div>
            </div>
          </div>
        </div>

        {/* Results panel */}
        <div className="lg:col-span-2 space-y-6">
          {/* Results panel */}
          <div className="bg-white shadow rounded-lg p-6">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-lg font-medium text-gray-900">Agent Results</h2>
              <button
                className="inline-flex items-center px-3 py-2 border border-gray-300 shadow-sm text-sm leading-4 font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                onClick={() => queryClient.invalidateQueries({ queryKey: ['agent-executions'] })}
              >
                <ArrowPathIcon className="-ml-0.5 mr-2 h-4 w-4" aria-hidden="true" />
                Refresh
              </button>
            </div>

            {/* Result display */}
            <div className="border rounded-lg p-4 bg-gray-50">
              {executeAgentMutation.data ? (
                <div className="space-y-4">
                  <div>
                    <h3 className="text-md font-medium text-gray-900 mb-2">Generated Email Draft</h3>
                    <div className="whitespace-pre-line bg-white p-4 rounded border">
                      {executeAgentMutation.data.draft_email}
                    </div>
                  </div>
                  
                  <div>
                    <h3 className="text-md font-medium text-gray-900 mb-2">Research Results</h3>
                    <div className="bg-white p-4 rounded border">
                      <p><span className="font-semibold">Company:</span> {executeAgentMutation.data.research_results.company_info.name}</p>
                      <p><span className="font-semibold">Industry:</span> {executeAgentMutation.data.research_results.company_info.industry}</p>
                      <p><span className="font-semibold">Size:</span> {executeAgentMutation.data.research_results.company_info.size}</p>
                    </div>
                  </div>
                  
                  <div className="grid grid-cols-2 gap-4">
                    <div className="bg-white p-4 rounded border">
                      <p className="text-sm text-gray-600">Execution Time</p>
                      <p className="text-lg font-semibold">{executeAgentMutation.data.execution_time}s</p>
                    </div>
                    <div className="bg-white p-4 rounded border">
                      <p className="text-sm text-gray-600">Tokens Used</p>
                      <p className="text-lg font-semibold">{executeAgentMutation.data.tokens_used}</p>
                    </div>
                    <div className="bg-white p-4 rounded border">
                      <p className="text-sm text-gray-600">Cost</p>
                      <p className="text-lg font-semibold">${(executeAgentMutation.data.cost_cents / 100).toFixed(2)}</p>
                    </div>
                    <div className="bg-white p-4 rounded border">
                      <p className="text-sm text-gray-600">Status</p>
                      <p className="text-lg font-semibold text-green-600">Success</p>
                    </div>
                  </div>
                </div>
              ) : (
                <div className="text-center py-8">
                  <DocumentTextIcon className="mx-auto h-12 w-12 text-gray-400" />
                  <h3 className="mt-2 text-sm font-medium text-gray-900">No agent results yet</h3>
                  <p className="mt-1 text-sm text-gray-500">
                    Execute an agent to see results here
                  </p>
                </div>
              )}
            </div>
          </div>

          {/* Recent executions */}
          <div className="bg-white shadow rounded-lg p-6">
            <h2 className="text-lg font-medium text-gray-900 mb-4">Recent Executions</h2>
            {executionsLoading ? (
              <div className="animate-pulse p-4 text-center">
                <div className="h-4 bg-gray-200 rounded w-1/4 mx-auto mb-4"></div>
                <div className="h-4 bg-gray-200 rounded w-3/4 mx-auto"></div>
              </div>
            ) : (
              <ul className="divide-y divide-gray-200">
                {executions?.slice(0, 5).map((execution) => (
                  <li key={execution.id} className="py-4">
                    <div className="flex items-center justify-between">
                      <div className="text-sm font-medium text-indigo-600 truncate">
                        {execution.agent_type} agent
                      </div>
                      <div className="ml-2 flex-shrink-0 flex">
                        <span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${getStatusColor(execution.success)}`}>
                          {execution.success ? 'Success' : 'Failed'}
                        </span>
                      </div>
                    </div>
                    <div className="mt-2 flex justify-between text-sm text-gray-500">
                      <p>${(execution.cost_cents / 100).toFixed(2)}</p>
                      <p>{new Date(execution.completed_at).toLocaleString()}</p>
                    </div>
                  </li>
                ))}
              </ul>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default AgentPage;