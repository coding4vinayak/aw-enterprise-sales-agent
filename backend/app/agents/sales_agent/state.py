from typing import TypedDict, List, Dict, Any, Optional
from datetime import datetime
from app.db.models.lead import Lead

class AgentState(TypedDict, total=False):
    """
    The complete state for the sales agent workflow
    """
    # Input parameters
    lead: Lead
    user_id: str
    tenant_id: str
    agent_type: str  # research, outreach, follow-up
    
    # Execution plan
    plan: List[str]
    current_step: str
    step_history: List[Dict[str, Any]]
    
    # Working memory
    research_results: Dict[str, Any]
    enriched_data: Dict[str, Any]
    draft_email: str
    verification_result: Dict[str, Any]
    
    # Execution context
    trajectory: List[Dict[str, Any]]  # For audit trail
    tokens_used: int
    execution_time: float
    success: bool
    error: Optional[str]
    
    # Cost tracking
    cost_cents: int