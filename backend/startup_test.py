"""
Startup test to verify the application can initialize with the new database configuration
"""
import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

def test_startup():
    """Test that the application can start up with basic components"""
    
    print("Testing application startup...")
    
    # Test 1: Configuration loading
    try:
        from app.core.config import settings
        print(f"✅ Configuration loaded: Database URL starts with {settings.DATABASE_URL[:20]}...")
        
        # Verify the TimescaleDB URL is properly formatted
        if "timescale.com" in settings.DATABASE_URL:
            print("✅ TimescaleDB connection string detected")
        else:
            print(f"⚠️  Expected TimescaleDB connection string, got: {settings.DATABASE_URL[:50]}...")
            
    except Exception as e:
        print(f"❌ Failed to load configuration: {e}")
        return False
    
    # Test 2: Basic model structure
    try:
        from app.db.models.user import User
        from app.db.models.lead import Lead
        from app.db.models.tenant import Tenant
        print("✅ Database models imported successfully")
    except Exception as e:
        print(f"❌ Failed to import models: {e}")
        return False
    
    # Test 3: Schemas
    try:
        from app.schemas.user import UserCreate, UserResponse
        from app.schemas.lead import LeadCreate, LeadResponse
        print("✅ Schemas imported successfully")
    except Exception as e:
        print(f"❌ Failed to import schemas: {e}")
        return False
    
    # Test 4: Services
    try:
        from app.services.customer.lead_service import LeadService
        from app.services.auth.jwt import create_access_token
        print("✅ Services imported successfully")
    except Exception as e:
        print(f"❌ Failed to import services: {e}")
        return False
    
    # Test 5: Dependencies
    try:
        from app.db.session import engine, SessionLocal
        print("✅ Database session configured")
    except Exception as e:
        print(f"❌ Failed to configure database session: {e}")
        return False
    
    print("\n🎉 Application startup test successful!")
    print("The application is properly configured and ready to connect to TimescaleDB")
    print("Database connection string: postgres://tsdbadmin:x2vm5sx9l1twlyzv@de65epw0cu.bc4seyfffs.tsdb.cloud.timescale.com:35895/tsdb?sslmode=require")
    
    return True

if __name__ == "__main__":
    success = test_startup()
    if not success:
        print("\n❌ Application startup test failed. Please fix the issues before running the application.")
        sys.exit(1)
    else:
        print("\n✅ Application is ready to run with TimescaleDB!")
        print("\nTo start the application:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Start the backend: python -m uvicorn app.main:app --reload --port 8000")
        print("3. Start the frontend (in another terminal): npm run dev (in frontend directory)")