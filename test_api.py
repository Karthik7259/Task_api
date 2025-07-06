"""
Test script for the Task Management REST API
Run this script after starting the Flask server to test all endpoints

This script tests the restructured API with proper separation of concerns:
- Routes in /routes
- Controllers in /controllers  
- Models in /models
- Configuration in /config
"""

import requests
import json
import time

BASE_URL = "http://localhost:5000"

def test_health_check():
    """Test the health check endpoint"""
    print("🔍 Testing health check...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to the API. Make sure the server is running on http://localhost:5000")
        return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False
    return True

def test_create_task():
    """Test creating a new task"""
    print("\n🔍 Testing task creation...")
    task_data = {
        "title": "Test Task 1",
        "description": "This is a test task for API testing"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/tasks", json=task_data)
        if response.status_code == 201:
            task = response.json()
            print("✅ Task created successfully")
            print(f"   Created task: {task}")
            return task['id']
        else:
            print(f"❌ Task creation failed: {response.status_code}")
            print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Task creation error: {e}")
    return None

def test_get_all_tasks():
    """Test getting all tasks"""
    print("\n🔍 Testing get all tasks...")
    try:
        response = requests.get(f"{BASE_URL}/tasks")
        if response.status_code == 200:
            tasks = response.json()
            print("✅ Get all tasks successful")
            print(f"   Found {len(tasks)} tasks")
            for task in tasks:
                print(f"   - Task {task['id']}: {task['title']}")
        else:
            print(f"❌ Get all tasks failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Get all tasks error: {e}")

def test_get_task_by_id(task_id):
    """Test getting a task by ID"""
    print(f"\n🔍 Testing get task by ID ({task_id})...")
    try:
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        if response.status_code == 200:
            task = response.json()
            print("✅ Get task by ID successful")
            print(f"   Task: {task}")
        else:
            print(f"❌ Get task by ID failed: {response.status_code}")
            print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Get task by ID error: {e}")

def test_update_task(task_id):
    """Test updating a task"""
    print(f"\n🔍 Testing task update ({task_id})...")
    update_data = {
        "title": "Updated Test Task",
        "description": "This task has been updated",
        "is_completed": True
    }
    
    try:
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=update_data)
        if response.status_code == 200:
            task = response.json()
            print("✅ Task update successful")
            print(f"   Updated task: {task}")
        else:
            print(f"❌ Task update failed: {response.status_code}")
            print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Task update error: {e}")

def test_filter_tasks():
    """Test filtering tasks by completion status"""
    print("\n🔍 Testing task filtering...")
    
    # Create another task for better testing
    task_data = {
        "title": "Test Task 2",
        "description": "Another test task",
        "is_completed": False
    }
    
    try:
        # Create second task
        requests.post(f"{BASE_URL}/tasks", json=task_data)
        
        # Test filter for completed tasks
        response = requests.get(f"{BASE_URL}/tasks?is_completed=true")
        if response.status_code == 200:
            completed_tasks = response.json()
            print(f"✅ Filter completed tasks successful: {len(completed_tasks)} tasks")
        
        # Test filter for pending tasks
        response = requests.get(f"{BASE_URL}/tasks?is_completed=false")
        if response.status_code == 200:
            pending_tasks = response.json()
            print(f"✅ Filter pending tasks successful: {len(pending_tasks)} tasks")
            
    except Exception as e:
        print(f"❌ Task filtering error: {e}")

def test_delete_task(task_id):
    """Test deleting a task"""
    print(f"\n🔍 Testing task deletion ({task_id})...")
    try:
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        if response.status_code == 200:
            print("✅ Task deletion successful")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Task deletion failed: {response.status_code}")
            print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Task deletion error: {e}")

def test_not_found():
    """Test 404 error handling"""
    print("\n🔍 Testing 404 error handling...")
    try:
        response = requests.get(f"{BASE_URL}/tasks/999")
        if response.status_code == 404:
            print("✅ 404 error handling works correctly")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Expected 404, got {response.status_code}")
    except Exception as e:
        print(f"❌ 404 test error: {e}")

def test_validation():
    """Test input validation"""
    print("\n🔍 Testing input validation...")
    
    # Test missing title
    invalid_data = {"description": "Missing title"}
    try:
        response = requests.post(f"{BASE_URL}/tasks", json=invalid_data)
        if response.status_code == 400:
            print("✅ Input validation works for missing title")
        else:
            print(f"❌ Expected 400 for missing title, got {response.status_code}")
    except Exception as e:
        print(f"❌ Validation test error: {e}")

def main():
    """Run all tests"""
    print("🚀 Starting Task Management API Tests")
    print("=" * 50)
    
    # Check if server is running
    if not test_health_check():
        print("\n❌ Cannot proceed with tests. Please start the Flask server first:")
        print("   python app.py")
        return
    
    # Run all tests
    task_id = test_create_task()
    if task_id:
        test_get_all_tasks()
        test_get_task_by_id(task_id)
        test_update_task(task_id)
        test_filter_tasks()
        test_not_found()
        test_validation()
        test_delete_task(task_id)
        
        # Final check
        print("\n🔍 Final check - getting all tasks...")
        test_get_all_tasks()
    
    print("\n" + "=" * 50)
    print("🏁 Test run completed!")

if __name__ == "__main__":
    main()
