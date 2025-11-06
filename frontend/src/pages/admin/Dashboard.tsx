import React from 'react';
import { 
  BuildingOfficeIcon, 
  UsersIcon, 
  ChatBubbleLeftRightIcon, 
  CurrencyDollarIcon,
  ChartBarIcon,
  ArrowTrendingUpIcon
} from '@heroicons/react/24/outline';

const AdminDashboard: React.FC = () => {
  // Mock data for admin metrics
  const adminMetrics = {
    totalTenants: 128,
    totalUsers: 1243,
    totalLeads: 24500,
    totalAgentExecutions: 18500,
    totalRevenue: 48560,
    monthlyGrowth: 12.5
  };

  // Mock data for recent activity
  const recentActivity = [
    { id: 1, user: 'John Smith', tenant: 'Acme Corp', action: 'Created new lead', time: '2 minutes ago' },
    { id: 2, user: 'Sarah Johnson', tenant: 'Tech Solutions', action: 'Executed outreach agent', time: '15 minutes ago' },
    { id: 3, user: 'Mike Williams', tenant: 'Global Inc', action: 'Updated CRM settings', time: '1 hour ago' },
    { id: 4, user: 'Admin User', tenant: 'Enterprise Ltd', action: 'Modified billing plan', time: '2 hours ago' },
    { id: 5, user: 'Emily Davis', tenant: 'Startup Tech', action: 'Completed campaign', time: '3 hours ago' },
  ];

  return (
    <div className="space-y-6">
      {/* Page header */}
      <div className="sm:flex sm:items-center">
        <div className="sm:flex-auto">
          <h1 className="text-xl font-semibold text-gray-900">Admin Dashboard</h1>
          <p className="mt-2 text-sm text-gray-700">
            Manage tenants, users, and monitor platform usage
          </p>
        </div>
      </div>

      {/* Stats grid */}
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3">
        <div className="bg-white overflow-hidden shadow rounded-lg">
          <div className="px-4 py-5 sm:p-6">
            <div className="flex items-center">
              <div className="flex-shrink-0 bg-indigo-500 rounded-md p-3">
                <BuildingOfficeIcon className="h-6 w-6 text-white" />
              </div>
              <div className="ml-5 w-0 flex-1">
                <dl>
                  <dt className="text-sm font-medium text-gray-500 truncate">Total Tenants</dt>
                  <dd className="flex items-baseline">
                    <div className="text-2xl font-semibold text-gray-900">
                      {adminMetrics.totalTenants}
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
                <UsersIcon className="h-6 w-6 text-white" />
              </div>
              <div className="ml-5 w-0 flex-1">
                <dl>
                  <dt className="text-sm font-medium text-gray-500 truncate">Total Users</dt>
                  <dd className="flex items-baseline">
                    <div className="text-2xl font-semibold text-gray-900">
                      {adminMetrics.totalUsers}
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
                  <dt className="text-sm font-medium text-gray-500 truncate">Agent Executions</dt>
                  <dd className="flex items-baseline">
                    <div className="text-2xl font-semibold text-gray-900">
                      {adminMetrics.totalAgentExecutions.toLocaleString()}
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
                <CurrencyDollarIcon className="h-6 w-6 text-white" />
              </div>
              <div className="ml-5 w-0 flex-1">
                <dl>
                  <dt className="text-sm font-medium text-gray-500 truncate">Revenue (YTD)</dt>
                  <dd className="flex items-baseline">
                    <div className="text-2xl font-semibold text-gray-900">
                      ${adminMetrics.totalRevenue.toLocaleString()}
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
              <div className="flex-shrink-0 bg-yellow-500 rounded-md p-3">
                <ArrowTrendingUpIcon className="h-6 w-6 text-white" />
              </div>
              <div className="ml-5 w-0 flex-1">
                <dl>
                  <dt className="text-sm font-medium text-gray-500 truncate">Monthly Growth</dt>
                  <dd className="flex items-baseline">
                    <div className="text-2xl font-semibold text-gray-900">
                      {adminMetrics.monthlyGrowth}%
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
              <div className="flex-shrink-0 bg-red-500 rounded-md p-3">
                <ChartBarIcon className="h-6 w-6 text-white" />
              </div>
              <div className="ml-5 w-0 flex-1">
                <dl>
                  <dt className="text-sm font-medium text-gray-500 truncate">Total Leads</dt>
                  <dd className="flex items-baseline">
                    <div className="text-2xl font-semibold text-gray-900">
                      {adminMetrics.totalLeads.toLocaleString()}
                    </div>
                  </dd>
                </dl>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Charts and activity */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Platform usage chart */}
        <div className="bg-white shadow overflow-hidden sm:rounded-lg">
          <div className="px-4 py-5 border-b border-gray-200 sm:px-6">
            <h3 className="text-lg leading-6 font-medium text-gray-900">Platform Usage</h3>
            <p className="mt-1 text-sm text-gray-500">Agent executions over the last 30 days</p>
          </div>
          <div className="p-6">
            {/* Chart placeholder */}
            <div className="h-64 flex items-center justify-center bg-gray-50 rounded-md">
              <div className="text-center">
                <ChartBarIcon className="mx-auto h-12 w-12 text-gray-400" />
                <p className="mt-2 text-sm text-gray-600">Usage chart visualization</p>
                <p className="text-xs text-gray-500">Would display actual chart data in production</p>
              </div>
            </div>
          </div>
        </div>

        {/* Recent activity */}
        <div className="bg-white shadow overflow-hidden sm:rounded-lg">
          <div className="px-4 py-5 border-b border-gray-200 sm:px-6">
            <h3 className="text-lg leading-6 font-medium text-gray-900">Recent Activity</h3>
            <p className="mt-1 text-sm text-gray-500">Latest actions across all tenants</p>
          </div>
          <ul className="divide-y divide-gray-200">
            {recentActivity.map((activity) => (
              <li key={activity.id} className="px-4 py-4 sm:px-6">
                <div className="flex items-center">
                  <div className="h-10 w-10 rounded-full bg-indigo-100 flex items-center justify-center">
                    <span className="text-indigo-800 font-bold">
                      {activity.user.charAt(0)}
                    </span>
                  </div>
                  <div className="ml-4">
                    <div className="text-sm font-medium text-gray-900">{activity.user}</div>
                    <div className="text-sm text-gray-500">
                      <span className="font-semibold">{activity.tenant}</span> - {activity.action}
                    </div>
                  </div>
                  <div className="ml-auto text-sm text-gray-500">
                    {activity.time}
                  </div>
                </div>
              </li>
            ))}
          </ul>
        </div>
      </div>

      {/* Quick stats */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white shadow rounded-lg p-6">
          <h3 className="text-lg font-medium text-gray-900 mb-2">Top Tenants</h3>
          <div className="space-y-3">
            <div className="flex justify-between">
              <span className="text-sm font-medium">TechCorp</span>
              <span className="text-sm text-gray-500">1,243 leads</span>
            </div>
            <div className="flex justify-between">
              <span className="text-sm font-medium">Global Inc</span>
              <span className="text-sm text-gray-500">987 leads</span>
            </div>
            <div className="flex justify-between">
              <span className="text-sm font-medium">Enterprise Solutions</span>
              <span className="text-sm text-gray-500">876 leads</span>
            </div>
          </div>
        </div>

        <div className="bg-white shadow rounded-lg p-6">
          <h3 className="text-lg font-medium text-gray-900 mb-2">Active Users</h3>
          <div className="space-y-3">
            <div className="flex justify-between">
              <span className="text-sm font-medium">Today</span>
              <span className="text-sm text-gray-500">452</span>
            </div>
            <div className="flex justify-between">
              <span className="text-sm font-medium">This Week</span>
              <span className="text-sm text-gray-500">1,234</span>
            </div>
            <div className="flex justify-between">
              <span className="text-sm font-medium">This Month</span>
              <span className="text-sm text-gray-500">5,678</span>
            </div>
          </div>
        </div>

        <div className="bg-white shadow rounded-lg p-6">
          <h3 className="text-lg font-medium text-gray-900 mb-2">System Health</h3>
          <div className="space-y-3">
            <div className="flex justify-between">
              <span className="text-sm font-medium">API Response Time</span>
              <span className="text-sm text-green-600">142ms</span>
            </div>
            <div className="flex justify-between">
              <span className="text-sm font-medium">Success Rate</span>
              <span className="text-sm text-green-600">99.7%</span>
            </div>
            <div className="flex justify-between">
              <span className="text-sm font-medium">Uptime</span>
              <span className="text-sm text-green-600">99.95%</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;