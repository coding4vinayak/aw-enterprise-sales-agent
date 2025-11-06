import React, { Fragment, useState } from 'react';
import { Menu, Transition } from '@headlessui/react';
import { 
  UserCircleIcon, 
  Cog6ToothIcon, 
  ArrowRightStartOnRectangleIcon,
  BuildingOfficeIcon
} from '@heroicons/react/24/outline';
import { User } from '../../types';

interface UserMenuProps {
  user: User | null;
  onLogout: () => void;
}

const UserMenu: React.FC<UserMenuProps> = ({ user, onLogout }) => {
  const [isLoggingOut, setIsLoggingOut] = useState(false);

  const handleLogout = async () => {
    setIsLoggingOut(true);
    try {
      onLogout();
    } finally {
      setIsLoggingOut(false);
    }
  };

  return (
    <Menu as="div" className="relative ml-3">
      <div>
        <Menu.Button className="max-w-xs flex rounded-full bg-white text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
          <span className="sr-only">Open user menu</span>
          <div className="h-8 w-8 rounded-full bg-indigo-500 flex items-center justify-center">
            <UserCircleIcon className="h-6 w-6 text-white" aria-hidden="true" />
          </div>
        </Menu.Button>
      </div>
      <Transition
        as={Fragment}
        enter="transition ease-out duration-100"
        enterFrom="transform opacity-0 scale-95"
        enterTo="transform opacity-100 scale-100"
        leave="transition ease-in duration-75"
        leaveFrom="transform opacity-100 scale-100"
        leaveTo="transform opacity-0 scale-95"
      >
        <Menu.Items className="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg py-1 bg-white ring-1 ring-black ring-opacity-5 focus:outline-none z-50">
          <div className="px-4 py-2 border-b border-gray-200">
            <p className="text-sm font-medium text-gray-900 truncate">
              {user?.name || 'User'}
            </p>
            <p className="text-xs text-gray-500 truncate">
              {user?.email || 'No email'}
            </p>
            <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-indigo-100 text-indigo-800 mt-1">
              {user?.role?.toUpperCase() || 'USER'}
            </span>
          </div>
          <Menu.Item>
            {({ active }) => (
              <a
                href="/settings"
                className={`${
                  active ? 'bg-gray-100' : ''
                } group flex items-center px-4 py-2 text-sm text-gray-700`}
              >
                <Cog6ToothIcon
                  className="mr-3 h-5 w-5 text-gray-400 group-hover:text-gray-500"
                  aria-hidden="true"
                />
                Settings
              </a>
            )}
          </Menu.Item>
          <Menu.Item>
            {({ active }) => (
              <a
                href="/admin"
                className={`${
                  active ? 'bg-gray-100' : ''
                } group flex items-center px-4 py-2 text-sm text-gray-700 ${
                  user?.role !== 'owner' && user?.role !== 'admin' ? 'hidden' : ''
                }`}
              >
                <BuildingOfficeIcon
                  className="mr-3 h-5 w-5 text-gray-400 group-hover:text-gray-500"
                  aria-hidden="true"
                />
                Admin Panel
              </a>
            )}
          </Menu.Item>
          <Menu.Item>
            {({ active }) => (
              <button
                onClick={handleLogout}
                disabled={isLoggingOut}
                className={`${
                  active ? 'bg-gray-100' : ''
                } w-full text-left group flex items-center px-4 py-2 text-sm text-gray-700`}
              >
                <ArrowRightStartOnRectangleIcon
                  className="mr-3 h-5 w-5 text-gray-400 group-hover:text-gray-500"
                  aria-hidden="true"
                />
                {isLoggingOut ? 'Logging out...' : 'Sign out'}
              </button>
            )}
          </Menu.Item>
        </Menu.Items>
      </Transition>
    </Menu>
  );
};

export default UserMenu;