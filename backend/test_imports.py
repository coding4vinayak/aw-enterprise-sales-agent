"""
Test script to verify all imports work correctly
"""
import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

def test_imports():
    """Test that all important modules can be imported without errors"""
    
    print("Testing backend imports...")
    
    # Core modules
    try:
        from app.main import app
        print("✅ Main app imported successfully")
    except Exception as e:
        print(f"❌ Failed to import main app: {e}")
        return False
    
    try:
        from app.core.config import settings
        print("✅ Config imported successfully")
    except Exception as e:
        print(f"❌ Failed to import config: {e}")
        return False
    
    # Models
    try:
        from app.db.models.user import User
        from app.db.models.lead import Lead
        from app.db.models.tenant import Tenant
        from app.db.models.campaign import Campaign, CampaignStep, CampaignAssignment
        from app.db.models.agent_execution import AgentExecution
        print("✅ All models imported successfully")
    except Exception as e:
        print(f"❌ Failed to import models: {e}")
        return False
    
    # Schemas
    try:
        from app.schemas.user import UserCreate, UserResponse
        from app.schemas.lead import LeadCreate, LeadResponse
        from app.schemas.campaign import CampaignCreate, CampaignResponse
        from app.schemas.tenant import TenantCreate, TenantResponse
        print("✅ All schemas imported successfully")
    except Exception as e:
        print(f"❌ Failed to import schemas: {e}")
        return False
    
    # Services
    try:
        from app.services.customer.lead_service import LeadService
        from app.services.customer.campaign_service import CampaignService
        from app.services.admin.user_service import UserService
        from app.services.admin.tenant_service import TenantService
        from app.services.admin.usage_service import UsageService
        print("✅ All services imported successfully")
    except Exception as e:
        print(f"❌ Failed to import services: {e}")
        return False
    
    # API endpoints
    try:
        from app.api.v1.endpoints import auth, customer, admin
        from app.api.v1.endpoints.customer import leads, agent, campaigns, crm
        from app.api.v1.endpoints.admin import users, tenants, usage, crm_config
        print("✅ All API endpoints imported successfully")
    except Exception as e:
        print(f"❌ Failed to import API endpoints: {e}")
        return False
    
    # Agents
    try:
        from app.agents.sales_agent.graph import SalesAgent
        from app.agents.sales_agent.state import AgentState
        print("✅ All agents imported successfully")
    except Exception as e:
        print(f"❌ Failed to import agents: {e}")
        return False
    
    # Observability
    try:
        from app.observability.metrics import agent_executions_total
        from app.observability.tracing import instrument_app
        from app.observability.logging import setup_logging
        print("✅ All observability modules imported successfully")
    except Exception as e:
        print(f"❌ Failed to import observability modules: {e}")
        return False
    
    print("\n🎉 All imports successful! The backend is properly structured and all modules are connected.")
    return True

if __name__ == "__main__":
    success = test_imports()
    if not success:
        print("\n❌ There were import errors. Please fix them before running the application.")
        sys.exit(1)
    else:
        print("\n✅ Application is ready to run!")