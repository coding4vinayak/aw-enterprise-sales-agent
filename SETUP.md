# Enterprise Sales Agent - Setup Guide

## Prerequisites

- Python 3.9+ (for backend)
- Node.js 16+ and npm (for frontend)
- PostgreSQL 12+ (or TimescaleDB)
- Docker and Docker Compose (optional, for containerized setup)
- Git

## Environment Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd aw-enterprise-sales-agent
```

### 2. Backend Setup

#### Python Environment
```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install backend dependencies
pip install -r requirements.txt
```

#### Environment Configuration
Create a `.env` file in the root directory with the following variables:

```bash
# Backend Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/enterprise_sales_agent
DATABASE_POOL_SIZE=20
DATABASE_POOL_OVERFLOW=10

# JWT Settings
SECRET_KEY=your-very-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# OpenAI Settings
OPENAI_API_KEY=your-openai-api-key
PRIMARY_MODEL=gpt-4o-mini
FALLBACK_MODEL=gpt-4o

# External API Settings
SERPAPI_API_KEY=your-serpapi-key
CLEARBIT_API_KEY=your-clearbit-key

# Redis Settings
REDIS_URL=redis://localhost:6379/0

# CORS Settings
BACKEND_CORS_ORIGINS=http://localhost,http://localhost:3000,http://localhost:8000

# Debug Settings
DEBUG=true
```

#### Database Setup
```bash
# Run database migrations
cd backend
python -m alembic upgrade head
```

#### Running the Backend
```bash
# From the project root
cd /workspaces/aw-enterprise-sales-agent
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Frontend Setup

#### Install Dependencies
```bash
cd frontend
npm install
```

#### Frontend Environment
Create a `.env` file in the `frontend` directory:

```bash
# API Configuration
VITE_API_URL=http://localhost:8000

# Debug Settings
VITE_DEBUG=true
```

#### Running the Frontend
```bash
# From the frontend directory
cd frontend
npm run dev -- --host 0.0.0.0 --port 3000
```

## Docker Setup (Alternative)

If you prefer using Docker, you can set up the application using Docker Compose:

```bash
# Using the provided docker-compose file
docker-compose up -d
```

This will start:
- PostgreSQL database
- Backend API server
- Frontend development server
- Redis (for caching/queue processing)

## Initial Configuration

### Database Initialization
The application will automatically create database tables on startup. In production, make sure to run migrations before starting the application:

```bash
cd backend
python -m alembic upgrade head
```

### Admin User Setup
On first run, you can create an admin user by registering through the web interface. The first user typically gets owner privileges.

## Development Setup

### Running Both Applications
To run both backend and frontend simultaneously during development:

**In separate terminals:**
```bash
# Terminal 1 - Backend
cd /workspaces/aw-enterprise-sales-agent
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2 - Frontend
cd /workspaces/aw-enterprise-sales-agent/frontend
npm run dev -- --host 0.0.0.0 --port 3000
```

### Development Tools
The project includes the following development tools:

- Backend:
  - FastAPI automatic documentation at `/docs` and `/redoc`
  - Pydantic for type validation
  - SQLAlchemy for ORM operations

- Frontend:
  - Vite for fast development builds
  - React Query for server state management
  - TypeScript for type safety
  - Tailwind CSS for styling

## Testing Setup

### Backend Tests
```bash
# Run backend tests
cd /workspaces/aw-enterprise-sales-agent
pytest
```

### Frontend Tests
```bash
# Run frontend tests
cd /workspaces/aw-enterprise-sales-agent/frontend
npm test
```

## Production Considerations

For production deployment, ensure you have:

1. **Proper Secret Management**: Use a secrets management system or environment variables
2. **HTTPS**: Implement SSL certificates for secure communication
3. **Database Backup**: Set up regular database backups
4. **Monitoring**: Implement application monitoring and alerting
5. **Security Headers**: Add security headers to HTTP responses
6. **Rate Limiting**: Configure appropriate rate limiting for APIs
7. **Caching**: Implement API response caching for better performance

## Verification

After setup, verify the installation:

1. Backend health check: `GET http://localhost:8000/api/v1/health`
2. Backend docs: `GET http://localhost:8000/docs`
3. Frontend: `GET http://localhost:3000/`

The application should be fully functional with:
- Working health check endpoint
- Interactive API documentation
- Accessible frontend with working registration/login
- Proper database connectivity