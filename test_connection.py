#!/usr/bin/env python3
"""
Test script to verify backend API connectivity
"""
import requests
import sys
import time

def test_backend_connection():
    """Test basic connection to backend API"""
    try:
        print("Testing backend connection...")
        response = requests.get("http://localhost:8000/api/v1/health", timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            print("✅ Backend connection successful!")
            return True
        else:
            print("❌ Backend connection failed!")
            return False
            
    except Exception as e:
        print(f"❌ Error connecting to backend: {e}")
        return False

def test_api_endpoints():
    """Test various API endpoints to ensure they're accessible"""
    endpoints = [
        "/api/v1/health",
        "/docs",  # OpenAPI docs
    ]
    
    for endpoint in endpoints:
        try:
            response = requests.get(f"http://localhost:8000{endpoint}", timeout=10)
            print(f"✅ {endpoint}: {response.status_code}")
        except Exception as e:
            print(f"❌ {endpoint}: {e}")

def main():
    print("Starting connection tests...")
    
    # Test backend connectivity
    if test_backend_connection():
        print("\nTesting various endpoints...")
        test_api_endpoints()
        
        print("\n✅ All connection tests completed successfully!")
        return True
    else:
        print("\n❌ Connection tests failed!")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)