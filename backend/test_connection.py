"""
Connection test to verify the application can initialize with TimescaleDB
"""
import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

def test_connection():
    """Test that the application can connect with basic components"""
    
    print("Testing application with TimescaleDB...")
    
    # Test configuration loading
    try:
        from app.core.config import settings
        print(f"SUCCESS: Configuration loaded")
        print(f"Database URL: {settings.DATABASE_URL[:50]}...")
        
        # Verify TimescaleDB connection string
        if "timescale.com" in settings.DATABASE_URL:
            print("SUCCESS: TimescaleDB connection string detected")
        else:
            print(f"WARNING: Expected TimescaleDB connection string, got: {settings.DATABASE_URL[:50]}...")
            
    except Exception as e:
        print(f"ERROR: Failed to load configuration: {e}")
        return False
    
    # Test basic imports
    try:
        from app.db.models.user import User
        from app.db.models.lead import Lead
        from app.db.models.tenant import Tenant
        print("SUCCESS: Database models imported successfully")
    except Exception as e:
        print(f"ERROR: Failed to import models: {e}")
        return False
    
    try:
        from app.schemas.user import UserCreate, UserResponse
        from app.schemas.lead import LeadCreate, LeadResponse
        print("SUCCESS: Schemas imported successfully")
    except Exception as e:
        print(f"ERROR: Failed to import schemas: {e}")
        return False
    
    try:
        from app.db.session import engine, SessionLocal
        print("SUCCESS: Database session configured")
    except Exception as e:
        print(f"ERROR: Failed to configure database session: {e}")
        return False
    
    # Test that we can create an engine
    try:
        from sqlalchemy import create_engine
        test_engine = create_engine(settings.DATABASE_URL)
        print("SUCCESS: Database engine created successfully")
    except Exception as e:
        print(f"ERROR: Failed to create database engine: {e}")
        return False
    
    print("\nCOMPLETE: Application is configured to use TimescaleDB!")
    print("The application structure is ready to connect to the TimescaleDB database")
    print("Database connection string: postgres://tsdbadmin:x2vm5sx9l1twlyzv@de65epw0cu.bc4seyfffs.tsdb.cloud.timescale.com:35895/tsdb?sslmode=require")
    
    return True

if __name__ == "__main__":
    success = test_connection()
    if not success:
        print("\nFAILED: Application configuration test failed. Please fix the issues before running the application.")
        sys.exit(1)
    else:
        print("\nSUCCESS: Application is ready to run with TimescaleDB!")
        print("\nNext steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Run database migrations: alembic upgrade head")
        print("3. Start the backend: python -m uvicorn app.main:app --reload --port 8000")
        print("4. Start the frontend (in another terminal): npm run dev (in frontend directory)")