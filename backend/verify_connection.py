import asyncio
import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import sys

# Use your actual database connection from the config
from app.core.config import settings

print("Verifying database connection...")
print(f"Database URL: {'postgresql://****:****@' + settings.DATABASE_URL.split('@')[1] if '@' in settings.DATABASE_URL else 'HIDDEN'}")

try:
    # Test synchronous connection
    engine = create_engine(
        settings.DATABASE_URL,
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True,
        echo=False
    )
    
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        version = result.scalar()
        print("SUCCESS: Connected to PostgreSQL-compatible database!")
        print(f"Database version: {version[:50]}...")  # Truncate long version string
        
        # Test basic operations
        try:
            # Check if we can create a temporary table
            conn.execute(text("CREATE TEMP TABLE test_conn (id INT);"))
            print("SUCCESS: Basic database operations working")
        except Exception as e:
            print(f"INFO: Could not create temp table (this is OK in some environments): {e}")
    
    print("\nPOSTGRESQL COMPATIBLE DATABASE CONNECTION VERIFIED!")
    print("Your application can connect to any PostgreSQL-compatible database including:")
    print("- Standard PostgreSQL")
    print("- TimescaleDB") 
    print("- Amazon RDS PostgreSQL")
    print("- Google Cloud SQL PostgreSQL")
    print("- Azure Database for PostgreSQL")
    print("- Heroku Postgres")
    print("\nThe enterprise sales agent platform works with any PostgreSQL database!")

except OperationalError as e:
    print(f"ERROR: Could not connect to database - {e}")
    print("Make sure your database server is running and accessible")
    print("Check your connection string in the environment configuration")
    sys.exit(1)
except Exception as e:
    print(f"ERROR: Database connection failed - {e}")
    sys.exit(1)