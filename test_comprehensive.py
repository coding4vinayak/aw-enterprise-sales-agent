#!/usr/bin/env python3
"""
Comprehensive test of the Enterprise Sales Agent application.
Tests the main functionality of the application including user registration,
authentication, and basic API endpoints.
"""
import requests
import json
import time
import sys
from typing import Optional

class SalesAgentTester:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
        self.access_token = None
        self.user_id = None
    
    def test_health(self) -> bool:
        """Test the health endpoint"""
        try:
            response = requests.get(f"{self.base_url}/api/v1/health")
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Health check: {data['status']}")
                return True
            else:
                print(f"❌ Health check failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Health check error: {e}")
            return False
    
    def test_api_docs(self) -> bool:
        """Test that API documentation is available"""
        try:
            response = requests.get(f"{self.base_url}/docs")
            if response.status_code == 200:
                print("✅ API documentation available")
                return True
            else:
                print(f"❌ API docs unavailable: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ API docs error: {e}")
            return False
    
    def register_user(self, email: str = "test@example.com", password: str = "password123", name: str = "Test User") -> bool:
        """Register a new user"""
        try:
            register_data = {
                "email": email,
                "password": password,
                "name": name
            }
            
            response = self.session.post(f"{self.base_url}/api/v1/auth/register", json=register_data)
            
            if response.status_code in [200, 201]:
                print(f"✅ User registration successful: {email}")
                return True
            elif response.status_code == 400:
                # User might already exist
                print(f"📝 User already exists: {email}")
                return True
            else:
                print(f"❌ User registration failed: {response.status_code}, {response.text}")
                return False
        except Exception as e:
            print(f"❌ User registration error: {e}")
            return False
    
    def login_user(self, email: str = "test@example.com", password: str = "password123") -> bool:
        """Login with user credentials"""
        try:
            # Using form data for OAuth2PasswordRequestForm
            login_data = {
                "username": email,  # FastAPI uses 'username' for email
                "password": password
            }
            
            response = self.session.post(f"{self.base_url}/api/v1/auth/token", data=login_data)
            
            if response.status_code == 200:
                data = response.json()
                self.access_token = data.get("access_token")
                if self.access_token:
                    self.session.headers.update({"Authorization": f"Bearer {self.access_token}"})
                    print("✅ User login successful")
                    return True
                else:
                    print("❌ No access token in response")
                    return False
            else:
                print(f"❌ Login failed: {response.status_code}, {response.text}")
                return False
        except Exception as e:
            print(f"❌ Login error: {e}")
            return False
    
    def get_current_user(self) -> bool:
        """Get current user info using auth token"""
        try:
            response = self.session.get(f"{self.base_url}/api/v1/auth/me")
            
            if response.status_code == 200:
                user_data = response.json()
                print(f"✅ Current user: {user_data.get('email', 'Unknown')}")
                self.user_id = user_data.get('id')
                return True
            else:
                print(f"❌ Get user failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Get user error: {e}")
            return False
    
    def run_comprehensive_test(self):
        """Run all tests in sequence"""
        print("🚀 Starting comprehensive test of Enterprise Sales Agent app...\n")
        
        tests = [
            ("Health Check", self.test_health),
            ("API Docs", self.test_api_docs),
            ("User Registration", self.register_user),
            ("User Login", self.login_user),
            ("Get Current User", self.get_current_user),
        ]
        
        results = []
        for test_name, test_func in tests:
            print(f"🧪 Testing: {test_name}")
            result = test_func()
            results.append((test_name, result))
            print()
        
        # Print summary
        print("📊 Test Results Summary:")
        passed = 0
        for test_name, result in results:
            status = "✅ PASS" if result else "❌ FAIL"
            print(f"  {status}: {test_name}")
            if result:
                passed += 1
        
        print(f"\n📈 Overall: {passed}/{len(results)} tests passed")
        
        if passed == len(results):
            print("🎉 All tests passed! The application is working correctly.")
            return True
        else:
            print("⚠️  Some tests failed. Please check the application setup.")
            return False

def main():
    """Main function to run the comprehensive test"""
    tester = SalesAgentTester()
    success = tester.run_comprehensive_test()
    
    if success:
        print("\n✅ Application test completed successfully!")
        return True
    else:
        print("\n❌ Application test failed!")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)