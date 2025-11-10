#!/usr/bin/env python3
"""
Simple test to check database connection
"""
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import os

# Create a test database connection
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/enterprise_sales_agent")

try:
    print("Attempting to connect to database...")
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("✅ Database connection successful!")
        print(f"Query result: {result.fetchone()}")
except SQLAlchemyError as e:
    print(f"❌ Database connection failed: {e}")
except Exception as e:
    print(f"❌ General error: {e}")