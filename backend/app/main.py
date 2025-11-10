from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router
from app.observability.health import router as health_router
from app.observability.middleware import MetricsMiddleware, TracingMiddleware, LoggingMiddleware
from app.observability.logging import setup_logging
from app.observability.tracing import instrument_app
from app.observability.alerting import ALERT_MANAGER
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base
import asyncio
import asyncpg
from sqlalchemy import text

def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application
    """
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json" if settings.DEBUG else None,
        docs_url="/docs" if settings.DEBUG else None,
        redoc_url="/redoc" if settings.DEBUG else None
    )
    
    # Setup logging
    setup_logging()
    
    # Add CORS middleware
    if settings.backend_cors_origins_list:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.backend_cors_origins_list],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    
    # Add observability middleware
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(MetricsMiddleware)
    app.add_middleware(TracingMiddleware)
    
    # Include routers
    app.include_router(api_router, prefix=settings.API_V1_STR)
    app.include_router(health_router, prefix=settings.API_V1_STR)
    
    # Instrument for tracing
    instrument_app(app)
    
    # Startup event
    @app.on_event("startup")
    async def startup_event():
        # Create database tables
        def create_tables():
            # Use the sync engine to create tables
            from app.db.session import engine
            from app.db.base import Base
            with engine.connect() as conn:
                Base.metadata.create_all(bind=conn)
        
        # Run sync operation in a thread pool
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, create_tables)
        
        # Start alert monitoring in background
        asyncio.create_task(ALERT_MANAGER.start_monitoring())
    
    # Shutdown event
    @app.on_event("shutdown")
    async def shutdown_event():
        # Stop alert monitoring
        ALERT_MANAGER.stop_monitoring()
    
    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=settings.DEBUG
    )