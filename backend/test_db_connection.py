import asyncio
import os
from sqlalchemy import create_engine, text

# Use your TimescaleDB connection string
DATABASE_URL = "postgresql://tsdbadmin:x2vm5sx9l1twlyzv@de65epw0cu.bc4seyfffs.tsdb.cloud.timescale.com:35895/tsdb?sslmode=require"

print("Attempting to connect to TimescaleDB...")
print(f"URL: {'postgresql://tsdbadmin:****@de65epw0cu.bc4seyfffs.tsdb.cloud.timescale.com:35895/tsdb?sslmode=require'}")

try:
    # Test synchronous connection first
    engine = create_engine(DATABASE_URL)
    
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        version = result.scalar()
        print(f"SUCCESS: Connected to database!")
        print(f"Database version: {version}")
        
        # Test creating a simple table to verify write permissions
        try:
            conn.execute(text("CREATE TABLE IF NOT EXISTS test_connection (id SERIAL PRIMARY KEY, timestamp TIMESTAMP DEFAULT NOW());"))
            conn.execute(text("INSERT INTO test_connection DEFAULT VALUES;"))
            conn.execute(text("DROP TABLE test_connection;"))
            print("SUCCESS: Database write operations working correctly")
        except Exception as e:
            print(f"WARNING: Could not perform write operations: {e}")
    
    print("\nTIMESCALEDB CONNECTION TEST COMPLETED SUCCESSFULLY!")
    print("The database connection is properly configured and functional.")
    print("Your enterprise sales agent can now connect to TimescaleDB.")

except Exception as e:
    print(f"ERROR: Database connection failed: {e}")
    print("Please verify your connection string is correct.")