# Minimal Setup Guide

This guide explains how to run the Enterprise Sales Agent application with a minimal configuration that excludes heavy packages like ML/AI libraries and observability tools.

## Files Included in Minimal Setup

### Backend
- `backend/app/main_minimal.py` - A minimal version of the main application without observability features
- `backend/requirements_minimal_final.txt` - Minimal dependencies without ML/AI or observability packages
- `infra/docker/Dockerfile.backend.minimal` - Dockerfile for the minimal backend

### Frontend
- `frontend/package.json.minimal` - Minimal dependencies for the frontend
- `frontend/Dockerfile.minimal` - Dockerfile for the minimal frontend

### Configuration
- `docker-compose-minimal-final.yml` - Docker Compose configuration with minimal services (no Jaeger or other observability tools)

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

### Heavy Document Processing
- lxml
- unstructured
- pypdf

## Running the Minimal Setup

### Using Docker Compose
```bash
docker-compose -f docker-compose-minimal-final.yml up --build
```

### Running Backend Only
```bash
cd backend
pip install -r requirements_minimal_final.txt
uvicorn app.main_minimal:app --host 0.0.0.0 --port 8000
```

### Running Frontend Only
```bash
cd frontend
npm install
npm run dev
```

## Services
- Backend API: http://localhost:8000
- Frontend: http://localhost:3000
- Database: PostgreSQL on localhost:5432
- Redis: on localhost:6379