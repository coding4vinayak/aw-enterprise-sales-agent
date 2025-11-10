# Enterprise Sales Agent - Minimal Setup

This document provides instructions for running the minimal version of the Enterprise Sales Agent application with heavy packages removed.

## What's Included in the Minimal Setup

### Backend
- Core FastAPI application (`app.main_minimal`)
- Essential dependencies only (no ML/AI or heavy observability packages)
- Database connectivity (PostgreSQL/pgvector)
- Redis connectivity
- Basic authentication and user management
- Health check endpoints

### Frontend
- Basic React application
- Essential dependencies only

### Services
- PostgreSQL database with pgvector extension
- Redis server
- Application backend

## Heavy Packages Removed

### ML/AI Libraries
- langchain, langgraph
- openai
- langchain-community, langchain-openai, langchain-core
- tiktoken
- faiss-cpu, sentence-transformers
- weaviate-client

### Observability Libraries
- opentelemetry-* packages
- prometheus-client
- sentry-sdk

### Document Processing
- lxml
- unstructured
- pypdf

## Running the Minimal Setup

### Prerequisites
- Docker and Docker Compose
- Git (to clone the repository if needed)

### Starting the Services

1. **Full minimal setup** (backend + frontend + dependencies):
   ```bash
   docker-compose -f docker-compose-minimal-final.yml up --build
   ```

2. **Backend only** (recommended for API testing):
   ```bash
   docker-compose -f docker-compose-minimal-final.yml up --build db redis backend
   ```

### API Endpoints
- Health check: `http://localhost:8000/api/v1/health`
- API documentation: `http://localhost:8000/api/v1/docs` (when DEBUG=true)

### Services
- Backend API: http://localhost:8000
- Frontend: http://localhost:3001 (if started)
- Database: PostgreSQL on localhost:5432
- Redis: on localhost:6379

### Key Files
- Backend: `backend/app/main_minimal.py`
- Backend requirements: `backend/requirements_minimal_final.txt`
- Frontend: `frontend/Dockerfile.minimal`
- Configuration: `docker-compose-minimal-final.yml`

## Testing the API

After starting the backend services, you can test the health endpoint:
```bash
curl http://localhost:8000/api/v1/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2025-11-10T10:35:07.246630",
  "service": "sales-agent-platform",
  "version": "1.0.0"
}
```

## Troubleshooting

1. **Port conflicts**: If you get port binding errors, ensure no other services are using ports 8000, 5432, 6379, or 3001
2. **Database migrations**: The application will attempt to create tables on startup
3. **Build errors**: Check that all dependencies are properly installed

## Development Notes

- The minimal setup is designed for core functionality testing
- Heavy features like AI/ML capabilities are excluded
- Observability features are removed for performance
- All configurations maintain security best practices