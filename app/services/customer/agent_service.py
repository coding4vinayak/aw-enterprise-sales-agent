from typing import List, Optional
from sqlalchemy.orm import Session
from datetime import datetime
from app.db.models.user import User
from app.db.models.lead import Lead
from app.db.models.agent_execution import AgentExecution
from app.schemas.agent import AgentExecutionResponse
from app.agents.sales_agent.graph import SalesAgent
from app.agents.sales_agent.state import AgentState
import uuid

class AgentService:
    def __init__(self, db: Session, user: User):
        self.db = db
        self.user = user
        self.tenant_id = user.tenant_id

    async def execute_agent(self, lead_id: str, agent_type: str = "research") -> Optional[AgentExecutionResponse]:
        """
        Execute a sales agent on a lead
        """
        # Get the lead
        lead = self.db.query(Lead).filter(
            Lead.id == lead_id,
            Lead.tenant_id == self.tenant_id
        ).first()
        
        if not lead:
            return None

        # Create initial state
        initial_state: AgentState = {
            "lead": lead,
            "user_id": str(self.user.id),
            "tenant_id": str(self.tenant_id),
            "agent_type": agent_type,
            "plan": [],
            "current_step": "initialized",
            "step_history": [],
            "research_results": {},
            "enriched_data": {},
            "draft_email": "",
            "verification_result": {},
            "trajectory": [],
            "tokens_used": 0,
            "execution_time": 0,
            "success": False,
            "error": None,
            "cost_cents": 0
        }

        # Execute the agent
        agent = SalesAgent()
        start_time = datetime.utcnow()
        result = await agent.run(initial_state)
        execution_time = (datetime.utcnow() - start_time).total_seconds()

        # Save execution record
        execution = AgentExecution(
            id=uuid.uuid4(),
            tenant_id=self.tenant_id,
            user_id=self.user.id,
            lead_id=lead_id,
            agent_type=agent_type,
            trajectory=str(result.get('trajectory', [])),
            success=result.get('success', False),
            tokens_input=result.get('tokens_used', 0),
            tokens_output=0,  # Would track output tokens separately
            cost_cents=result.get('cost_cents', 0),
            started_at=start_time,
            completed_at=datetime.utcnow()
        )
        
        self.db.add(execution)
        self.db.commit()
        self.db.refresh(execution)

        return AgentExecutionResponse(
            id=str(execution.id),
            tenant_id=str(execution.tenant_id),
            user_id=str(execution.user_id),
            lead_id=str(execution.lead_id),
            agent_type=execution.agent_type,
            trajectory=execution.trajectory or "",
            success=execution.success,
            tokens_input=execution.tokens_input,
            tokens_output=execution.tokens_output,
            cost_cents=execution.cost_cents,
            started_at=execution.started_at,
            completed_at=execution.completed_at,
            created_at=execution.created_at,
            updated_at=execution.updated_at
        )

    async def get_executions(
        self, 
        skip: int = 0, 
        limit: int = 50
    ) -> List[AgentExecutionResponse]:
        """
        Get agent execution history
        """
        executions = self.db.query(AgentExecution).filter(
            AgentExecution.tenant_id == self.tenant_id,
            AgentExecution.user_id == self.user.id
        ).order_by(AgentExecution.created_at.desc()).offset(skip).limit(limit).all()

        return [
            AgentExecutionResponse(
                id=str(exec.id),
                tenant_id=str(exec.tenant_id),
                user_id=str(exec.user_id),
                lead_id=str(exec.lead_id),
                agent_type=exec.agent_type,
                trajectory=exec.trajectory or "",
                success=exec.success,
                tokens_input=exec.tokens_input,
                tokens_output=exec.tokens_output,
                cost_cents=exec.cost_cents,
                started_at=exec.started_at,
                completed_at=exec.completed_at,
                created_at=exec.created_at,
                updated_at=exec.updated_at
            )
            for exec in executions
        ]

    async def get_execution(self, execution_id: str) -> Optional[AgentExecutionResponse]:
        """
        Get specific execution
        """
        execution = self.db.query(AgentExecution).filter(
            AgentExecution.id == execution_id,
            AgentExecution.tenant_id == self.tenant_id
        ).first()
        
        if not execution:
            return None
            
        return AgentExecutionResponse(
            id=str(execution.id),
            tenant_id=str(execution.tenant_id),
            user_id=str(execution.user_id),
            lead_id=str(execution.lead_id),
            agent_type=execution.agent_type,
            trajectory=execution.trajectory or "",
            success=execution.success,
            tokens_input=execution.tokens_input,
            tokens_output=execution.tokens_output,
            cost_cents=execution.cost_cents,
            started_at=execution.started_at,
            completed_at=execution.completed_at,
            created_at=execution.created_at,
            updated_at=execution.updated_at
        )