from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

class AgentExecutionBase(BaseModel):
    tenant_id: str
    user_id: str
    lead_id: str
    agent_type: str
    trajectory: Optional[str] = None
    success: bool
    tokens_input: int
    tokens_output: int
    cost_cents: int
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

class AgentExecutionCreate(AgentExecutionBase):
    pass

class AgentExecutionUpdate(BaseModel):
    success: Optional[bool] = None
    cost_cents: Optional[int] = None

class AgentExecutionResponse(AgentExecutionBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True