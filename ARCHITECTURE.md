# Enterprise Sales Agent - Architecture Documentation

## Overview
The Enterprise Sales Agent is a full-stack application designed to automate sales processes using AI agents. It features a React frontend with a FastAPI backend, PostgreSQL database, and comprehensive observability.

## System Architecture

### Frontend (React/Vite)
- Built with React 18 and TypeScript
- Uses React Router for client-side routing
- Implements Context API for state management
- Leverages Tailwind CSS for styling
- Uses React Query for data fetching and caching
- Follows component-based architecture

### Backend (FastAPI)
- Built with FastAPI framework for high performance
- Uses Pydantic for data validation
- Implements FastAPI security features
- Provides RESTful API with automatic OpenAPI docs

### Database (PostgreSQL/TimescaleDB)
- Uses SQLAlchemy ORM for database interactions
- Implements UUID primary keys
- Supports multi-tenancy
- JSONB fields for flexible data storage
- Proper indexing for performance

### AI Agent System
- Built with LangGraph for state management
- Implements research, outreach, and follow-up agents
- Tracks execution steps, costs, and tokens used
- Supports different agent types

## Component Architecture

### Frontend Structure
```
frontend/
├── public/                 # Static assets
├── src/
│   ├── components/         # Reusable UI components
│   ├── contexts/           # React Context providers
│   ├── layouts/            # Page layouts
│   ├── pages/              # Route components
│   ├── services/           # API services
│   ├── styles/             # Global styles
│   ├── types/              # TypeScript type definitions
│   └── utils/              # Utility functions
├── package.json            # Dependencies and scripts
└── vite.config.ts          # Build configuration
```

### Backend Structure
```
app/
├── agents/                 # AI agent implementations
│   └── sales_agent/
│       ├── graph.py        # Agent workflow
│       └── state.py        # Agent state definition
├── api/                    # API endpoints
│   └── v1/
│       ├── endpoints/      # Route handlers
│       │   ├── auth/       # Authentication
│       │   ├── admin/      # Admin functions
│       │   └── customer/   # Customer functions
│       └── v1.py           # API router
├── core/                   # Core application logic
│   ├── config.py          # Configuration
│   ├── security.py        # Security utilities
│   └── exceptions.py      # Custom exceptions
├── db/                     # Database models and session
│   ├── models/            # SQLAlchemy models
│   ├── base.py            # Base model
│   └── session.py         # Database session
├── schemas/                # Pydantic schemas
├── services/               # Business logic
├── observability/          # Logging, metrics, tracing
└── main.py                 # Application entry point
```

## Security Architecture

### Authentication
- JWT-based authentication with access/refresh tokens
- Password hashing with bcrypt
- Secure token storage and refresh mechanism
- Role-based access control (owner, admin, user)

### Authorization
- Multi-tenancy to isolate tenant data
- Protected API routes with dependency injection
- Database-level access controls

## API Architecture

### Versioning
- API versioned at `/api/v1/`
- All endpoints follow RESTful principles

### Authentication Flow
1. User registers/login via `/auth/register` or `/auth/token`
2. JWT token returned and stored client-side
3. Token sent in Authorization header for protected routes
4. Token validated by dependency injection in routes

## AI Agent Architecture

### State Management
- Uses LangGraph-style state management
- Tracks execution steps, costs, and tokens
- Maintains execution history for debugging

### Agent Types
- Research agents: Gather company and lead information
- Outreach agents: Generate personalized emails
- Follow-up agents: Handle follow-up sequences

## Observability

### Logging
- JSON-formatted structured logging
- Request/response logging with correlation IDs
- Error logging with context

### Metrics
- API request metrics (count, duration)
- Agent execution metrics (costs, tokens)
- Performance metrics per tenant

### Tracing
- Distributed tracing with OpenTelemetry
- Request spans for debugging
- Performance analysis capabilities

## Deployment Architecture

### Containerization
- Docker support for all components
- Separate images for frontend and backend
- Docker Compose for local development

### Scalability
- Stateful services (database) separated from stateless (API)
- Horizontal scaling for API tier
- Database connection pooling