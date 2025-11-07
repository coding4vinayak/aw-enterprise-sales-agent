from pydantic_settings import BaseSettings
from typing import Optional, List
import os

class Settings(BaseSettings):
    # App settings
    PROJECT_NAME: str = "Enterprise Sales Agent"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = False
    
    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://tsdbadmin:x2vm5sx9l1twlyzv@de65epw0cu.bc4seyfffs.tsdb.cloud.timescale.com:35895/tsdb?sslmode=require")
    DATABASE_POOL_SIZE: int = 20
    DATABASE_POOL_OVERFLOW: int = 10
    
    # JWT settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # OpenAI settings
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    PRIMARY_MODEL: str = os.getenv("PRIMARY_MODEL", "gpt-4o-mini")
    FALLBACK_MODEL: str = os.getenv("FALLBACK_MODEL", "gpt-4o")
    
    # External API settings
    SERPAPI_API_KEY: str = os.getenv("SERPAPI_API_KEY", "")
    CLEARBIT_API_KEY: str = os.getenv("CLEARBIT_API_KEY", "")
    
    # Redis settings
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    
    # Security
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost", "http://localhost:3000", "http://localhost:8000"]
    
    # Rate limiting
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_WINDOW: int = 60  # seconds
    
    # Tenant isolation
    MULTI_TENANCY: bool = True
    
    # Observability
    OTEL_EXPORTER_OTLP_ENDPOINT: str = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "")
    
    # File storage
    FILE_STORAGE_PATH: str = os.getenv("FILE_STORAGE_PATH", "./uploads")
    
    # Email settings
    SMTP_HOST: str = os.getenv("SMTP_HOST", "")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER: str = os.getenv("SMTP_USER", "")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")
    
    # OAuth settings
    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID", "")
    GOOGLE_CLIENT_SECRET: str = os.getenv("GOOGLE_CLIENT_SECRET", "")
    GITHUB_CLIENT_ID: str = os.getenv("GITHUB_CLIENT_ID", "")
    GITHUB_CLIENT_SECRET: str = os.getenv("GITHUB_CLIENT_SECRET", "")
    
    # SSO settings
    SSO_SAML_METADATA_URL: Optional[str] = os.getenv("SSO_SAML_METADATA_URL")
    
    # CRM settings
    DEFAULT_CRM_PROVIDER: str = os.getenv("DEFAULT_CRM_PROVIDER", "hubspot")
    
    class Config:
        env_file = ".env"

settings = Settings()