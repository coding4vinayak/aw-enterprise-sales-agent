import requests
import subprocess
import time
import signal
import os

def test_minimal_setup():
    """Test the minimal setup to ensure it works correctly"""
    
    # Start the minimal backend
    print("Starting minimal backend...")
    proc = subprocess.Popen([
        "uvicorn", 
        "app.main_minimal:app", 
        "--host", "0.0.0.0", 
        "--port", "8002"
    ], cwd="backend")
    
    # Give it some time to start
    time.sleep(5)
    
    try:
        # Test the health endpoint
        print("Testing health endpoint...")
        response = requests.get("http://localhost:8002/health", timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            print("✓ Minimal setup test passed!")
        else:
            print("✗ Minimal setup test failed!")
            
    except Exception as e:
        print(f"✗ Test failed with error: {e}")
    finally:
        # Stop the process
        proc.send_signal(signal.SIGTERM)
        proc.wait()
        print("Backend stopped.")

if __name__ == "__main__":
    test_minimal_setup()