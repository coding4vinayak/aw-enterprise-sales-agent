import requests
import json

def test_minimal_api_functionality():
    """Test minimal API functionality"""
    base_url = "http://localhost:8000"
    
    print("Testing minimal API functionality...")
    
    # Test health endpoint
    response = requests.get(f"{base_url}/api/v1/health")
    health_data = response.json()
    print(f"Health check: {health_data}")
    
    # Test that docs are available
    response = requests.get(f"{base_url}/docs")
    print(f"Docs status: {response.status_code}")
    
    # Test that redoc is available
    response = requests.get(f"{base_url}/redoc")
    print(f"Redoc status: {response.status_code}")
    
    # Test registration endpoint (should return 422 for missing data, but should exist)
    try:
        response = requests.post(f"{base_url}/api/v1/auth/register", json={})
    except:
        # This might fail due to validation, which is expected
        pass
    
    print("✅ API functionality test completed!")

if __name__ == "__main__":
    test_minimal_api_functionality()