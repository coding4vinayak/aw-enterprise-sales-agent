# Enterprise Sales Agent - Deployment Guide

## Deployment Options

This guide covers multiple deployment approaches for different environments and requirements.

## 1. Production Deployment Architecture

### Recommended Architecture
```
Internet
  ↓
Load Balancer/Reverse Proxy (nginx/traefik)
  ↓
Multiple Backend API Instances
  ↓
PostgreSQL Database Cluster (Primary + Replica)
  ↓
Redis Cluster (for caching and queue processing)
```

### Containerized Deployment
```
Docker Swarm / Kubernetes
  ├─ Backend API Service (multiple replicas)
  ├─ Frontend Service (static files)
  ├─ PostgreSQL Service (with persistence)
  ├─ Redis Service
  └─ Optional: Queue Worker Service
```

## 2. Environment Variables for Production

### Backend Environment Variables
```bash
# Database Configuration (Production)
DATABASE_URL=postgresql://username:password@host:5432/dbname
DATABASE_POOL_SIZE=20
DATABASE_POOL_OVERFLOW=10

# JWT Configuration (Production)
SECRET_KEY=your-very-long-production-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# OpenAI Configuration
OPENAI_API_KEY=your-production-openai-key
PRIMARY_MODEL=gpt-4o
FALLBACK_MODEL=gpt-4

# External Services
SERPAPI_API_KEY=your-serpapi-key
CLEARBIT_API_KEY=your-clearbit-key

# Redis Configuration
REDIS_URL=redis://host:6379/0

# CORS Configuration
BACKEND_CORS_ORIGINS=https://yourdomain.com,https://app.yourdomain.com

# Security & Debug
DEBUG=false
ALLOWED_HOSTS=yourdomain.com,api.yourdomain.com

# Email Configuration (Production)
SMTP_HOST=smtp.yourprovider.com
SMTP_PORT=587
SMTP_USER=your-smtp-user
SMTP_PASSWORD=your-smtp-password

# Observability
OTEL_EXPORTER_OTLP_ENDPOINT=otel-collector:4317

# Rate Limiting
RATE_LIMIT_REQUESTS=1000
RATE_LIMIT_WINDOW=3600  # 1 hour

# Security
SECURE_SSL_REDIRECT=true
SECURE_HSTS_SECONDS=31536000
SECURE_BROWSER_XSS_FILTER=true
SECURE_CONTENT_TYPE_NOSNIFF=true
</pre>

### Frontend Environment Variables
```bash
# API Configuration
VITE_API_URL=https://api.yourdomain.com

# Debug Settings
VITE_DEBUG=false

# Analytics
VITE_GA_MEASUREMENT_ID=your-google-analytics-id

# Feature Flags
VITE_FEATURE_NEW_DASHBOARD=true
```

## 3. Docker Deployment

### Using Docker Compose (Staging/Production)
Create a `docker-compose.prod.yml` file:

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:13
    restart: always
    environment:
      POSTGRES_DB: enterprise_sales_agent
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    restart: always
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  backend:
    build:
      context: .
      dockerfile: Dockerfile.backend
    restart: always
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@postgres:5432/enterprise_sales_agent
      - REDIS_URL=redis://redis:6379/0
      - SECRET_KEY=${SECRET_KEY}
      - DEBUG=false
    ports:
      - "8000:8000"
    depends_on:
      - postgres
      - redis
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/api/v1/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.frontend
    restart: always
    ports:
      - "3000:80"
    environment:
      - VITE_API_URL=https://api.yourdomain.com

volumes:
  postgres_data:
  redis_data:
```

### Running the Production Stack
```bash
# Pull the latest code
git pull origin main

# Build and start services
docker-compose -f docker-compose.prod.yml up --build -d

# Run database migrations
docker-compose -f docker-compose.prod.yml exec backend python -m alembic upgrade head
```

## 4. Cloud Provider Deployments

### AWS Deployment
1. Use AWS RDS for PostgreSQL
2. Deploy backend to AWS ECS/EKS or AWS Lambda (with container support)
3. Serve frontend from S3 with CloudFront
4. Use AWS ElastiCache for Redis

### Google Cloud Platform
1. Use Cloud SQL for PostgreSQL
2. Deploy backend to Cloud Run or GKE
3. Serve frontend from Cloud Storage with CDN
4. Use Memorystore for Redis

### Azure
1. Use Azure Database for PostgreSQL
2. Deploy backend to Azure App Service or AKS
3. Serve frontend from Azure Static Web Apps or Storage
4. Use Azure Cache for Redis

## 5. Configuration Management

### Database Migrations in Production
```bash
# Before deploying new version with schema changes
# 1. Backup database
# 2. Deploy new code with migration scripts
# 3. Run migrations
alembic upgrade head

# For rollback capability
alembic downgrade -1
```

### Environment-Specific Configurations
Create multiple configuration files:
- `.env.production`
- `.env.staging`
- `.env.development`

## 6. Security Considerations

### HTTPS Setup
```bash
# Using nginx as reverse proxy with Let's Encrypt
server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com;

    ssl_certificate /path/to/certificate.crt;
    ssl_certificate_key /path/to/private.key;

    location / {
        proxy_pass http://frontend:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /api/ {
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Security Headers
- Implement Content Security Policy (CSP)
- Enable HSTS
- Add XSS protection headers
- Implement CSRF protection

## 7. Monitoring and Logging

### Application Monitoring
```bash
# Health checks
GET /api/v1/health - Overall health
GET /api/v1/health/ready - Readiness for traffic
GET /api/v1/health/live - Liveness probe

# Metrics endpoint
GET /metrics - Prometheus metrics
```

### Log Aggregation
- Centralized logging with tools like ELK stack or similar
- Structured JSON logs for easier parsing
- Log retention policies

## 8. Backup and Recovery

### Database Backup Strategy
```bash
# Daily automated backups
pg_dump -h hostname -U username -d database_name > backup.sql

# Or use cloud provider's automated backup features
```

### Recovery Procedures
1. Document recovery procedures with runbooks
2. Test backup restoration regularly
3. Have staging environment identical to production for testing

## 9. Scaling Considerations

### Horizontal Scaling
- Use a load balancer to distribute requests
- Implement sessionless authentication (JWT tokens)
- Use Redis for shared session/caching
- Database read replicas for read-heavy operations

### Performance Optimization
- Implement caching strategies
- Optimize database queries with proper indexing
- Use CDN for static assets
- Implement API response caching where appropriate

## 10. Deployment Checklist

- [ ] Database backups created before deployment
- [ ] Health checks passing
- [ ] Environment variables configured
- [ ] SSL certificates in place
- [ ] Monitoring configured
- [ ] Rollback plan ready
- [ ] Load testing completed
- [ ] Security scan passed
- [ ] Documentation updated
- [ ] Team notified of deployment