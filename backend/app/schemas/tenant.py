from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

class TenantBase(BaseModel):
    name: str
    subdomain: Optional[str] = None
    plan: str = "free"
    billing_email: Optional[str] = None

class TenantCreate(TenantBase):
    pass

class TenantUpdate(BaseModel):
    name: Optional[str] = None
    plan: Optional[str] = None
    billing_email: Optional[str] = None
    config: Optional[Dict[str, Any]] = None
    limits: Optional[Dict[str, Any]] = None

class TenantResponse(TenantBase):
    id: str
    status: str
    config: Optional[Dict[str, Any]] = None
    limits: Optional[Dict[str, Any]] = None
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True