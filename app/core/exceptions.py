"""
Custom exceptions for the application
"""

class LeadNotFoundException(Exception):
    """Raised when a lead is not found"""
    def __init__(self, lead_id: str):
        self.lead_id = lead_id
        super().__init__(f"Lead with ID {lead_id} not found")

class AgentExecutionException(Exception):
    """Raised when an agent execution fails"""
    def __init__(self, message: str):
        super().__init__(message)

class CRMIntegrationException(Exception):
    """Raised when CRM integration fails"""
    def __init__(self, message: str):
        super().__init__(message)

class TenantNotFoundException(Exception):
    """Raised when a tenant is not found"""
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id
        super().__init__(f"Tenant with ID {tenant_id} not found")

class UserNotFoundException(Exception):
    """Raised when a user is not found"""
    def __init__(self, user_id: str):
        self.user_id = user_id
        super().__init__(f"User with ID {user_id} not found")

class UnauthorizedException(Exception):
    """Raised when a user is not authorized to perform an action"""
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(message)