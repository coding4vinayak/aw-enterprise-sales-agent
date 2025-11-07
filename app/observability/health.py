from fastapi import APIRouter
from typing import Dict, Any
from datetime import datetime

router = APIRouter()

@router.get("/health")
async def health_check() -> Dict[str, Any]:
    """
    Overall health check endpoint
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "sales-agent-platform",
        "version": "1.0.0"
    }

@router.get("/health/ready")
async def readiness_check() -> Dict[str, str]:
    """
    Readiness check - used for container orchestration
    """
    return {"status": "ready"}

@router.get("/health/live")
async def liveness_check() -> Dict[str, str]:
    """
    Liveness check - indicates if the service is alive
    """
    return {"status": "alive"}