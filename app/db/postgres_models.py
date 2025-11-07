from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey, JSON, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

Base = declarative_base()

class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    subdomain = Column(String, unique=True, index=True)
    plan = Column(String, default="free")
    status = Column(String, default="active")
    config = Column(JSON)
    limits = Column(JSON)
    billing_email = Column(String)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    users = relationship("User", back_populates="tenant")
    leads = relationship("Lead", back_populates="tenant")
    agent_executions = relationship("AgentExecution", back_populates="tenant")

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user")  # owner, admin, user, viewer
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    last_login_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    tenant = relationship("Tenant", back_populates="users")
    leads = relationship("Lead", back_populates="user")
    agent_executions = relationship("AgentExecution", back_populates="user")

class Lead(Base):
    __tablename__ = "leads"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    email = Column(String, index=True)
    name = Column(String)
    company = Column(String, index=True)
    domain = Column(String, index=True)
    title = Column(String)
    linkedin_url = Column(String)
    phone = Column(String)
    status = Column(String, default="new")  # new, contacted, qualified, closed
    source = Column(String, default="agent")  # agent, import, form, etc.
    enriched_data = Column(JSON)
    crm_contact_id = Column(String)  # ID in external CRM
    crm_account_id = Column(String)  # ID in external CRM
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    tenant = relationship("Tenant", back_populates="leads")
    user = relationship("User", back_populates="leads")
    agent_executions = relationship("AgentExecution", back_populates="lead")

class AgentExecution(Base):
    __tablename__ = "agent_executions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    lead_id = Column(UUID(as_uuid=True), ForeignKey("leads.id"), nullable=False)
    agent_type = Column(String, nullable=False)  # research, outreach, follow-up, etc.
    trajectory = Column(JSON)  # Execution steps and results
    success = Column(Boolean, default=False)
    tokens_input = Column(Integer, default=0)
    tokens_output = Column(Integer, default=0)
    cost_cents = Column(Integer, default=0)  # Cost in cents
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    tenant = relationship("Tenant", back_populates="agent_executions")
    user = relationship("User", back_populates="agent_executions")
    lead = relationship("Lead", back_populates="agent_executions")

# Create indices for common queries
from sqlalchemy import Index

# Index for performance on commonly queried fields
Index('idx_leads_tenant_status', Lead.tenant_id, Lead.status)
Index('idx_leads_domain', Lead.domain)
Index('idx_agent_executions_tenant_type', AgentExecution.tenant_id, AgentExecution.agent_type)
Index('idx_users_tenant_role', User.tenant_id, User.role)