from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class UsageMetricsResponse(BaseModel):
    date_range: tuple[datetime, datetime]
    granularity: str
    metrics: List[Dict[str, Any]]
    totals: Dict[str, Any]

class TenantUsageResponse(BaseModel):
    tenant_id: str
    tenant_name: Optional[str] = None
    total_usage: int
    total_cost: float
    active_users: int
    task_count: int

class UsageExportResponse(BaseModel):
    filename: str
    download_url: str
    size: int
    created_at: datetime