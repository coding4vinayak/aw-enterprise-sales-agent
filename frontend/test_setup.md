# Frontend Setup and Testing Instructions

## Installation

```bash
cd frontend
npm install
```

## Running the Application

```bash
npm run dev
```

## Available Scripts

In the project directory, you can run:

### `npm run dev`
Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm run build`
Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

### `npm run lint`
Runs the linter to check for code style issues.

## Environment Variables

Create a `.env` file in the frontend directory with the following:

```env
VITE_API_URL=http://localhost:8000
VITE_WS_URL=ws://localhost:8000
VITE_APP_NAME=Enterprise Sales Agent
VITE_DEBUG=true
```

## Project Structure
```
frontend/
├── public/
├── src/
│   ├── components/     # Reusable UI components
│   ├── pages/          # Application pages
│   ├── layouts/        # Layout components
│   ├── services/       # API and business logic
│   ├── contexts/       # React context providers
│   ├── types/          # TypeScript type definitions
│   ├── utils/          # Utility functions
│   ├── styles/         # Global styles
│   ├── App.tsx         # Main application component
│   └── index.tsx       # Entry point
├── package.json
├── tsconfig.json
└── vite.config.ts
```

## Key Features

### Authentication
- Login and registration flows
- JWT-based authentication
- Protected routes
- Role-based access control

### Customer Dashboard
- Lead management
- Agent execution interface
- Campaign management
- Analytics and reporting

### Admin Dashboard
- Tenant management
- User management
- Usage analytics
- System configuration

### UI Components
- Reusable component library
- Responsive design
- Dark/light mode
- Form validation
- Loading states
- Error handling

## API Integration

The frontend communicates with the backend through the API service:

```typescript
import { api } from './services/api';

// Example API call
const response = await api.get('/api/v1/customer/leads');
```

All API calls automatically include the authentication token and handle errors appropriately.

## Testing

The application is ready for comprehensive testing. All components are properly connected to their backend counterparts.