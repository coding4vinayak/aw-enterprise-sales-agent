# Enterprise Sales Agent - Troubleshooting Guide

## Common Issues and Solutions

### 1. Application Startup Issues

#### Backend Fails to Start
**Symptoms:**
- Application crashes on startup
- Error messages about database connection
- Import errors

**Solutions:**
1. **Database Connection Issues:**
   ```bash
   # Check if database is running
   docker exec -i sales-agent-db pg_isready
   
   # Verify database URL in .env file
   echo $DATABASE_URL
   
   # Check database logs
   docker logs sales-agent-db
   ```

2. **Dependency Issues:**
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt
   
   # Check for conflicting versions
   pip list | grep -E "(fastapi|sqlalchemy|pydantic)"
   ```

3. **Environment Variables Missing:**
   ```bash
   # Verify required environment variables
   python -c "from app.core.config import settings; print(settings.DATABASE_URL)"
   ```

#### Frontend Fails to Start
**Symptoms:**
- Vite dev server doesn't start
- Build fails
- Routing issues

**Solutions:**
1. **Node Version Issues:**
   ```bash
   # Check Node.js version
   node --version
   
   # Clear npm cache
   npm cache clean --force
   
   # Delete node_modules and reinstall
   rm -rf node_modules package-lock.json
   npm install
   ```

### 2. Database Issues

#### Migration Problems
**Symptoms:**
- Alembic migration errors
- Database schema mismatch
- Duplicate migration files

**Solutions:**
1. **Check current migration state:**
   ```bash
   python -m alembic current
   ```

2. **If migrations are out of sync:**
   ```bash
   # Mark current state without applying changes
   python -m alembic stamp head
   
   # Or create a new migration
   python -m alembic revision --autogenerate -m "fix migration"
   python -m alembic upgrade head
   ```

#### Connection Pool Issues
**Symptoms:**
- Database timeout errors
- "Too many connections" errors
- Slow query performance

**Solutions:**
1. **Check connection settings in .env:**
   ```
   DATABASE_POOL_SIZE=20
   DATABASE_POOL_OVERFLOW=10
   ```

2. **Optimize connection usage:**
   - Ensure database sessions are properly closed
   - Check for connection leaks in application logs

### 3. Authentication Issues

#### Login Fails
**Symptoms:**
- Authentication returns 401 Unauthorized
- Token generation fails
- User registration issues

**Solutions:**
1. **Check user credentials:**
   ```bash
   # Verify user exists in database
   docker exec -it sales-agent-db psql -U postgres -d enterprise_sales_agent -c "SELECT * FROM users LIMIT 5;"
   ```

2. **Verify JWT settings:**
   ```bash
   python -c "from app.core.config import settings; print(settings.SECRET_KEY)"
   ```

3. **Check password hashing:**
   - Ensure passwords are properly hashed before storing
   - Verify bcrypt configuration

#### Token Refresh Issues
**Symptoms:**
- Access tokens expire too quickly
- Refresh token invalidation
- Session management problems

**Solutions:**
1. **Adjust token expiration settings in .env:**
   ```
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   REFRESH_TOKEN_EXPIRE_DAYS=7
   ```

### 4. API Issues

#### CORS Errors
**Symptoms:**
- Cross-origin requests blocked
- Frontend can't connect to backend
- Console error: "CORS policy blocked"

**Solutions:**
1. **Check CORS settings in .env:**
   ```
   BACKEND_CORS_ORIGINS=http://localhost:3000,http://localhost:8000
   ```

2. **Verify origin headers in requests**

#### API Response Issues
**Symptoms:**
- Malformed responses
- Validation errors
- Missing data

**Solutions:**
1. **Check Pydantic schema validation:**
   - Verify input/output schemas match requirements
   - Check for type mismatches

2. **Debug with logging:**
   ```python
   # Enable debug logging
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

### 5. Frontend Issues

#### Routing Problems
**Symptoms:**
- 404 errors for valid routes
- Router not handling paths correctly
- Links not working

**Solutions:**
1. **Verify React Router configuration:**
   - Check route definitions in `App.tsx`
   - Ensure protected routes work correctly

2. **Client-side vs server-side routing:**
   - For production, ensure server handles all routes to serve `index.html`

#### API Connection Issues
**Symptoms:**
- Frontend can't reach backend API
- Network timeout errors
- CORS issues

**Solutions:**
1. **Check API base URL in frontend:**
   ```bash
   # Verify VITE_API_URL in frontend/.env
   echo $VITE_API_URL
   ```

2. **Verify backend is running:**
   ```bash
   curl http://localhost:8000/api/v1/health
   ```

### 6. Performance Issues

#### Slow API Responses
**Symptoms:**
- High latency API calls
- Database queries taking too long
- Resource-heavy operations

**Solutions:**
1. **Database optimization:**
   - Add proper indexes
   - Optimize queries
   - Use connection pooling

2. **Application caching:**
   - Implement Redis caching
   - Use response caching for static data

#### Memory Issues
**Symptoms:**
- High memory usage
- Application crashes due to memory
- Slow performance over time

**Solutions:**
1. **Monitor memory usage:**
   ```bash
   # Check memory usage of processes
   ps aux | grep -E "(python|node|uvicorn)"
   ```

2. **Optimize code:**
   - Fix memory leaks
   - Use generators for large datasets
   - Implement proper resource cleanup

### 7. AI Agent Issues

#### Agent Execution Failures
**Symptoms:**
- Agent execution returns errors
- AI API calls failing
- Token cost tracking issues

**Solutions:**
1. **Check AI API configuration:**
   ```bash
   # Verify OpenAI API key
   python -c "from app.core.config import settings; print('Key set:' if settings.OPENAI_API_KEY else 'Key not set')"
   ```

2. **Debug agent state:**
   - Check agent state management
   - Verify execution steps
   - Monitor token usage

#### Research Agent Problems
**Symptoms:**
- Lead enrichment not working
- Data gathering failures
- Integration errors

**Solutions:**
1. **Check external API keys:**
   ```
   SERPAPI_API_KEY=your-serpapi-key
   CLEARBIT_API_KEY=your-clearbit-key
   ```

### 8. Logging and Monitoring

#### Log Issues
**Symptoms:**
- Missing log entries
- Incorrect log levels
- No structured logging

**Solutions:**
1. **Check logging configuration:**
   ```python
   # Verify logging setup
   import logging
   logger = logging.getLogger(__name__)
   logger.info("Test log message")
   ```

2. **Review log levels:**
   - Check DEBUG setting in environment
   - Verify log level filtering

#### Metric Collection Issues
**Symptoms:**
- Missing metrics
- Incomplete monitoring data
- Tracing not working

**Solutions:**
1. **Verify observability setup:**
   - Check OpenTelemetry configuration
   - Ensure metrics endpoints are accessible

### 9. Deployment Issues

#### Container Issues
**Symptoms:**
- Docker containers failing to start
- Network connectivity problems
- Volume mounting issues

**Solutions:**
1. **Check container logs:**
   ```bash
   docker logs <container_name>
   docker logs <container_name> --tail 50
   ```

2. **Verify Docker network:**
   ```bash
   docker network ls
   docker network inspect <network_name>
   ```

#### Build Issues
**Symptoms:**
- Docker build failures
- Compilation errors
- Missing dependencies

**Solutions:**
1. **Clean build cache:**
   ```bash
   docker system prune -a
   docker build --no-cache -t app:latest .
   ```

### 10. Debugging Techniques

#### Backend Debugging
```bash
# Enable debug mode
export DEBUG=true

# Run with detailed logging
python -m uvicorn app.main:app --reload --log-level debug

# Check application state
python -c "from app.main import app; print(app.routes)"
```

#### Frontend Debugging
```bash
# Enable React development mode
npm run dev

# Check browser console for errors
# Use React DevTools for component inspection
# Enable network tab for API debugging
```

#### Database Debugging
```bash
# Connect to database
docker exec -it sales-agent-db psql -U postgres -d enterprise_sales_agent

# Check table structure
\dt
\d+ table_name

# Run test queries
SELECT * FROM users LIMIT 5;
```

### 11. Emergency Procedures

#### Application Recovery
1. **Immediate actions:**
   - Check health endpoints
   - Review logs for errors
   - Verify service dependencies

2. **Rollback procedure:**
   - Deploy previous stable version
   - Restore from backup if needed
   - Notify stakeholders

#### Data Recovery
1. **Database recovery:**
   - Restore from latest backup
   - Check data integrity
   - Verify application functionality

### 12. Common Commands for Troubleshooting

```bash
# Check running processes
ps aux | grep -E "(python|uvicorn|node|vite)"

# Check network connections
netstat -tuln | grep -E "(3000|8000)"

# Check disk space
df -h

# Check memory usage
free -h

# Monitor application logs
tail -f /var/log/application.log

# Restart services
sudo systemctl restart <service_name>

# Check Docker containers
docker ps -a
docker logs <container_id>
```

### 13. Contact and Escalation

If issues persist after following these troubleshooting steps:

1. **Development team:** [Contact information]
2. **DevOps team:** [Contact information]
3. **Vendor support:** [For specific services like OpenAI, etc.]
4. **Infrastructure team:** [For hosting/infrastructure issues]