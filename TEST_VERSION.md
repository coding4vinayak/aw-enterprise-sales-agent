# Minimum Viable Test Version - Enterprise Sales Agent

This is a basic test version of the Enterprise Sales Agent application demonstrating the connection between frontend and backend.

## Architecture

- **Backend**: FastAPI server running on http://localhost:8000
- **Frontend**: React app running on http://localhost:3000
- **Database**: PostgreSQL (configured in backend/.env)

## Services Status

- ✅ Backend API running on port 8000
- ✅ Frontend development server running on port 3000
- ✅ Health check endpoint available at `/api/v1/health`
- ✅ Database tables created
- ✅ API documentation available at `/docs`

## Quick Test

You can verify the backend is working by making a request to the health endpoint:

```bash
curl http://localhost:8000/api/v1/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "...",
  "service": "sales-agent-platform",
  "version": "1.0.0"
}
```

## API Endpoints Available

- `GET /api/v1/health` - Health check
- `GET /docs` - Interactive API documentation
- `GET /redoc` - Alternative API documentation

## Frontend-Backend Integration

The frontend is configured to connect to the backend API. When the frontend makes requests to API endpoints, they will be forwarded to the backend service running on port 8000.

## Next Steps

For full functionality, you would need to:
1. Complete user registration and authentication flow
2. Set up proper database with real data
3. Configure AI services (OpenAI, etc.)
4. Connect CRM systems

## Troubleshooting

If you encounter issues:
1. Verify the backend server is running: `ps aux | grep uvicorn`
2. Check the backend logs
3. Verify the frontend is running: `lsof -i :3000`
4. Check CORS configuration in the backend