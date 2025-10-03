import subprocess
import sys
import os
import time
import webbrowser
import requests

def run_backend():
    """Start backend server using current Python environment"""
    backend_path = os.path.join(os.getcwd(), "backend")
    python_exe = sys.executable
    backend_cmd = [python_exe, "-m", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
    
    if os.name == 'nt':  # Windows
        subprocess.Popen(backend_cmd, cwd=backend_path, creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:  # Mac/Linux
        subprocess.Popen(["gnome-terminal", "--"] + backend_cmd, cwd=backend_path)

def run_frontend():
    """Start frontend server"""
    frontend_path = os.path.join(os.getcwd(), "frontend")
    frontend_cmd = ["npm", "start"]
    
    if os.name == 'nt':  # Windows
        subprocess.Popen(frontend_cmd, cwd=frontend_path, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:  # Mac/Linux
        subprocess.Popen(["gnome-terminal", "--", "npm", "start"], cwd=frontend_path)

def wait_for_api(url, timeout=60):
    """Wait for API to be ready"""
    print(f"\n⏳ Waiting for API to be ready...")
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                print("✅ Backend API is ready!")
                return True
        except (requests.ConnectionError, requests.Timeout):
            print(".", end="", flush=True)
            time.sleep(1)
    
    print("\n❌ Backend API failed to start")
    return False

def wait_for_frontend(url, timeout=60):
    """Wait for frontend to be ready"""
    print(f"⏳ Waiting for Frontend to be ready...")
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url, timeout=2)
            if response.status_code in [200, 304]:
                print("✅ Frontend is ready!")
                return True
        except (requests.ConnectionError, requests.Timeout):
            print(".", end="", flush=True)
            time.sleep(1)
    
    print("\n❌ Frontend failed to start")
    return False

if __name__ == "__main__":
    print("=" * 60)
    print(" 🚗 Vehicle Classification App")
    print("=" * 60)
    
    print("\n[1/3] 🔧 Starting Backend Server...")
    run_backend()
    time.sleep(2)
    
    print("[2/3] 🎨 Starting Frontend Server...")
    run_frontend()
    time.sleep(2)
    
    # Wait for backend API to be ready
    backend_ready = wait_for_api("http://localhost:8000/api/health")
    
    if backend_ready:
        # Wait for frontend to be ready
        frontend_ready = wait_for_frontend("http://localhost:3000")
        
        if frontend_ready:
            print("\n" + "=" * 60)
            print(" ✅ All servers are ready!")
            print("=" * 60)
            print(" 🌐 Backend API:  http://localhost:8000")
            print(" 🌐 Frontend App: http://localhost:3000")
            print(" 📚 API Docs:     http://localhost:8000/docs")
            print("=" * 60)
            
            # AUTOMATICALLY OPEN BROWSER
            print("\n[3/3] 🌐 Opening browser automatically...")
            time.sleep(1)
            webbrowser.open("http://localhost:3000")
            
            print("\n✅ Browser opened! Enjoy your app! 🚀")
            print("💡 Close both command windows to stop servers.")
            print("=" * 60)
