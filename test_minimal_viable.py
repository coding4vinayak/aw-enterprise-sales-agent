#!/usr/bin/env python3
"""
Simple test client that demonstrates frontend-backend connection
"""
import requests
import time
import json

class TestClient:
    def __init__(self, backend_url="http://localhost:8000"):
        self.backend_url = backend_url
        
    def run_test_suite(self):
        """Run a suite of tests to verify the connection"""
        print("🧪 Running Enterprise Sales Agent Test Suite\n")
        
        tests = [
            self.test_health_endpoint,
            self.test_api_docs,
            self.test_redoc,
            self.test_specific_endpoints,
        ]
        
        results = []
        for test in tests:
            try:
                result = test()
                results.append(result)
                print(f"✅ {test.__name__}: {'PASSED' if result[1] else 'FAILED'} - {result[0]}")
            except Exception as e:
                results.append(("Error", False, str(e)))
                print(f"❌ {test.__name__}: FAILED - {e}")
            print()
        
        # Summary
        passed = sum(1 for _, success, _ in results if success)
        total = len(results)
        
        print(f"📊 Test Results: {passed}/{total} tests passed")
        
        if passed == total:
            print("🎉 All tests passed! The frontend-backend connection is working properly.")
            print("\n📋 Available endpoints:")
            print("   • Health: http://localhost:8000/api/v1/health")
            print("   • API Docs: http://localhost:8000/docs")
            print("   • ReDoc: http://localhost:8000/redoc")
            return True
        else:
            print(f"⚠️  {total - passed} tests failed. Please check the setup.")
            return False
    
    def test_health_endpoint(self):
        """Test the health endpoint"""
        try:
            response = requests.get(f"{self.backend_url}/api/v1/health", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'healthy':
                    return ("Health check successful", True, data)
                else:
                    return ("Health check returned unhealthy status", False, data)
            else:
                return (f"Health endpoint returned {response.status_code}", False, response.text)
        except requests.exceptions.ConnectionError:
            return ("Cannot connect to backend", False, None)
        except Exception as e:
            return (f"Error testing health endpoint: {str(e)}", False, None)
    
    def test_api_docs(self):
        """Test the API documentation endpoint"""
        try:
            response = requests.get(f"{self.backend_url}/docs", timeout=10)
            if response.status_code == 200:
                return ("API Documentation available", True, "OK")
            else:
                return (f"API docs returned {response.status_code}", False, response.text)
        except Exception as e:
            return (f"Error testing API docs: {str(e)}", False, None)
    
    def test_redoc(self):
        """Test the ReDoc endpoint"""
        try:
            response = requests.get(f"{self.backend_url}/redoc", timeout=10)
            if response.status_code == 200:
                return ("ReDoc available", True, "OK")
            else:
                return (f"ReDoc returned {response.status_code}", False, response.text)
        except Exception as e:
            return (f"Error testing ReDoc: {str(e)}", False, None)
    
    def test_specific_endpoints(self):
        """Test other important endpoints"""
        endpoints_to_test = [
            "/api/v1/health",
            "/openapi.json"  # This might only be available in DEBUG mode
        ]
        
        all_passed = True
        details = {}
        
        for endpoint in endpoints_to_test:
            try:
                response = requests.get(f"{self.backend_url}{endpoint}", timeout=10)
                status = response.status_code
                details[endpoint] = status
                # For openapi.json, we consider it OK if it's available or if it's not enabled (e.g., in production mode)
                if endpoint == "/openapi.json" and status in [200, 404]:
                    # 404 is acceptable for openapi.json in non-debug mode
                    details[endpoint] = f"Status {status} (acceptable)"
                elif status != 200:
                    all_passed = False
                    details[endpoint] = f"Status {status} (not acceptable)"
            except Exception as e:
                details[endpoint] = f"Error: {str(e)}"
                all_passed = False
        
        return (f"Specific endpoints test - {details}", all_passed, details)

def main():
    client = TestClient()
    success = client.run_test_suite()
    
    if success:
        print("\n✅ Minimum viable test version is working correctly!")
        print("The frontend and backend are properly connected.")
    else:
        print("\n❌ Test version has issues that need to be addressed.")
    
    return success

if __name__ == "__main__":
    main()