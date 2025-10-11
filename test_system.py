#!/usr/bin/env python3
"""
Complete system test for Crop Diagnosis System
"""
import requests
import os
import sys

def test_system():
    print("🧪 Testing Complete Crop Diagnosis System")
    print("=" * 50)
    
    backend_url = "http://localhost:5000"
    
    # Test 1: Check if models exist
    print("\n1. Checking model files...")
    models = [
        os.path.join("models", "model1_multicrop.h5"),
        os.path.join("models", "model2_staple_crops.h5"), 
        os.path.join("models", "model3_banana.h5")
    ]
    
    models_found = 0
    for model_path in models:
        if os.path.exists(model_path):
            print(f"✅ {model_path} - Found")
            models_found += 1
        else:
            print(f"❌ {model_path} - Missing")
    
    print(f"Models found: {models_found}/3")
    
    # Test 2: Check backend health
    print("\n2. Testing backend connection...")
    try:
        response = requests.get(f"{backend_url}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Backend is running")
            print(f"   Status: {data.get('status')}")
            print(f"   Models loaded: {data.get('models_count', 0)}/3")
        else:
            print(f"❌ Backend returned status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Backend connection failed: {e}")
        print("   Make sure to run: start.bat")
    
    # Test 3: Check model endpoints
    print("\n3. Testing model endpoints...")
    try:
        response = requests.get(f"{backend_url}/test-models", timeout=5)
        if response.status_code == 200:
            models_data = response.json()
            print("✅ Model endpoint accessible")
            for model_name, status in models_data.items():
                status_icon = "✅" if status.get('loaded') else "❌"
                print(f"   {status_icon} {model_name}: {status.get('status', 'unknown')}")
        else:
            print(f"❌ Model endpoint failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Model endpoint error: {e}")
    
    # Test 4: Check frontend files
    print("\n4. Checking frontend files...")
    frontend_files = [
        "frontend/index.html",
        "frontend/multicrop.html",
        "frontend/staple.html",
        "frontend/banana.html"
    ]
    
    frontend_ok = True
    for file_path in frontend_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} - Found")
        else:
            print(f"❌ {file_path} - Missing")
            frontend_ok = False
    
    # Test 5: Dashboard test
    print("\n5. Testing backend dashboard...")
    try:
        response = requests.get(backend_url, timeout=5)
        if response.status_code == 200:
            print("✅ Backend dashboard accessible")
            print(f"   URL: {backend_url}")
        else:
            print(f"❌ Dashboard failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Dashboard error: {e}")
    
    # Summary
    print("\n" + "=" * 50)
    print("🎯 System Status Summary:")
    print(f"   Models: {models_found}/3 found")
    print(f"   Backend: {'✅ Running' if 'response' in locals() and response.status_code == 200 else '❌ Not running'}")
    print(f"   Frontend: {'✅ Ready' if frontend_ok else '❌ Missing files'}")
    
    print("\n📋 Next Steps:")
    if models_found < 3:
        print("   - Place your .h5 model files in the models/ directory")
    print("   - Run: start_complete_system.bat (to start backend)")
    print("   - Open frontend pages:")
    print("     • Main: frontend/index.html")
    print("     • Multi-crop: frontend/multicrop.html") 
    print("     • Staple crops: frontend/staple.html")
    print("     • Banana: frontend/banana.html")
    print("   - Backend dashboard: http://localhost:5000")

if __name__ == "__main__":
    test_system()