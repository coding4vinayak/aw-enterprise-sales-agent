import asyncio
import os
from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import QueuePool

# Use any PostgreSQL connection string
# This could be TimescaleDB, standard PostgreSQL, or any compatible database
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://username:password@localhost:5432/database_name")

print("Attempting to connect to PostgreSQL...")
# Extract host part to mask credentials in output
if '@' in DATABASE_URL:
    host_part = DATABASE_URL.split('@')[1]
    print(f"URL: postgresql://****:****@{host_part}")
else:
    print(f"URL: {DATABASE_URL}")

try:
    # Test synchronous connection first
    engine = create_engine(
        DATABASE_URL,
        poolclass=QueuePool,
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True,  # Validates connections before use
        echo=False  # Set to True for SQL debugging
    )
    
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        version = result.scalar()
        print(f"✅ Successfully connected to PostgreSQL!")
        print(f"📊 Database version: {version}")
        
        # Check if pgvector extension is available (needed for embeddings)
        try:
            pgvector_result = conn.execute(text("SELECT extname FROM pg_extension WHERE extname = 'vector';"))
            pgvector_available = pgvector_result.fetchone()
            if pgvector_available:
                print("✅ pgvector extension available (for embeddings)")
            else:
                print("⚠️  pgvector extension not found (embeddings will not work)")
        except Exception as e:
            print(f"⚠️  Could not check pgvector extension: {e}")
        
        # Test creating a simple table to verify write permissions
        try:
            conn.execute(text("CREATE TABLE IF NOT EXISTS test_connection (id SERIAL PRIMARY KEY, timestamp TIMESTAMP DEFAULT NOW());"))
            conn.execute(text("INSERT INTO test_connection DEFAULT VALUES;"))
            conn.execute(text("DROP TABLE test_connection;"))
            print("✅ Database write operations working correctly")
        except Exception as e:
            print(f"⚠️  Could not perform write operations: {e}")
    
    print("\n🎉 PostgreSQL connection test completed successfully!")
    print("The database connection is properly configured and functional.")
    print("Your enterprise sales agent can now connect to any PostgreSQL-compatible database.")

except Exception as e:
    print(f"❌ Database connection failed: {e}")
    print("Please verify your PostgreSQL connection string is correct.")
    print("Format: postgresql://username:password@host:port/database_name")