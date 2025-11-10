from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router
from app.observability.health import router as health_router
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base
import asyncio
from sqlalchemy import text

def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application (minimal version)
    """
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json" if settings.DEBUG else None,
        docs_url="/docs" if settings.DEBUG else None,
        redoc_url="/redoc" if settings.DEBUG else None
    )

    # Add CORS middleware
    if settings.backend_cors_origins_list:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.backend_cors_origins_list],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    # Include routers
    app.include_router(api_router, prefix=settings.API_V1_STR)
    app.include_router(health_router, prefix=settings.API_V1_STR)

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

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main_minimal:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )