#!/usr/bin/env python3
"""
Simple test script for the Crime Rate Prediction API
Run this script to test if your API is working correctly
"""

import requests
import json
import time

def test_api():
    """Test the Crime Rate Prediction API"""
    
    # API endpoint
    base_url = "http://localhost:8000"
    
    # Test data
    test_data = {
        "City": "Metropolis",
        "ARSON": 10,
        "ASSAULT": 85,
        "BURGLARY": 120,
        "COUNTERFEITING": 5,
        "CYBERCRIME": 40,
        "DRUG_OFFENSE": 70,
        "EXTORTION": 3,
        "FIREARM_OFFENSE": 12,
        "FRAUD": 30,
        "ROBBERY": 25,
        "SHOPLIFTING": 55,
        "TRAFFIC_VIOLATION": 200,
        "VANDALISM": 35,
        "VEHICLE_THEFT": 28,
        "Population": 500000,
        "Unemployment_Rate": 6.5,
        "Literacy_Rate": 92.3,
        "Total_Crimes": 718
    }
    
    print("🚀 Testing Crime Rate Prediction API")
    print("=" * 50)
    
    # Test 1: Health Check
    print("\n1. Testing Health Check...")
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed. Make sure the API is running on http://localhost:8000")
        return False
    
    # Test 2: Prediction Endpoint
    print("\n2. Testing Prediction Endpoint...")
    try:
        start_time = time.time()
        response = requests.post(f"{base_url}/predict", json=test_data)
        end_time = time.time()
        
        if response.status_code == 200:
            print("✅ Prediction successful")
            result = response.json()
            print(f"   Random Forest: {result['random_forest_prediction']}")
            print(f"   XGBoost: {result['xgboost_prediction']}")
            print(f"   KNN: {result['knn_prediction']}")
            print(f"   Ensemble: {result['ensemble_prediction']}")
            print(f"   Response Time: {(end_time - start_time)*1000:.2f}ms")
        else:
            print(f"❌ Prediction failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return False
    
    # Test 3: Invalid Data
    print("\n3. Testing Invalid Data Handling...")
    invalid_data = test_data.copy()
    invalid_data["Population"] = "invalid"  # String instead of int
    
    try:
        response = requests.post(f"{base_url}/predict", json=invalid_data)
        if response.status_code == 422:  # Validation error
            print("✅ Invalid data handling working correctly")
        else:
            print(f"⚠️  Unexpected response for invalid data: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Invalid data test failed: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 API testing completed successfully!")
    return True

def test_model_files():
    """Check if all required model files exist"""
    print("\n🔍 Checking Model Files...")
    
    required_files = [
        "models/random_forest.pkl",
        "models/xgModel.pkl", 
        "models/knnModel.pkl",
        "models/city_encoder.pkl",
        "models/knnFeatures.pkl"
    ]
    
    missing_files = []
    for file_path in required_files:
        try:
            with open(file_path, 'rb') as f:
                print(f"✅ {file_path}")
        except FileNotFoundError:
            print(f"❌ {file_path} - MISSING")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n⚠️  Missing {len(missing_files)} model files")
        print("   Make sure to place all .pkl files in the models/ directory")
        return False
    else:
        print("\n✅ All model files present")
        return True

if __name__ == "__main__":
    print("Crime Rate Prediction API - Test Suite")
    print("Make sure the API is running with: uvicorn app:app --reload")
    print()
    
    # Check model files first
    if not test_model_files():
        print("\n❌ Cannot proceed without model files")
        exit(1)
    
    # Test API
    if test_api():
        print("\n🎯 All tests passed! Your API is working correctly.")
    else:
        print("\n💥 Some tests failed. Check the errors above.")
        exit(1)
