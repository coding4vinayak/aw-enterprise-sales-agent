from pydantic_settings import BaseSettings
from typing import List
import os

# Set environment variable with comma-separated values
os.environ['BACKEND_CORS_ORIGINS'] = 'http://localhost,http://localhost:3000,http://localhost:8000'

class Settings(BaseSettings):
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost", "http://localhost:3000", "http://localhost:8000"]

    class Config:
        env_nested_delimiter = ','  # Configure delimiter for list parsing

settings = Settings()
print("Parsed CORS origins:", settings.BACKEND_CORS_ORIGINS)