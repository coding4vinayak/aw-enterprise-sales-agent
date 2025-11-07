from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

class AuditLogBase(BaseModel):
    tenant_id: str
    user_id: Optional[str] = None
    action: str
    resource_type: str
    resource_id: str
    changes_before: Optional[Dict[str, Any]] = None
    changes_after: Optional[Dict[str, Any]] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    previous_hash: Optional[str] = None
    current_hash: Optional[str] = None

class AuditLogCreate(AuditLogBase):
    pass

class AuditLogResponse(AuditLogBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

class AuditLogSummary(BaseModel):
    total_logs: int
    action_counts: Dict[str, int]
    resource_type_counts: Dict[str, int]
    date_range: Dict[str, str]