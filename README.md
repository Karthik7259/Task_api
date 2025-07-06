# Task Management REST API

A simple REST API built with Flask that allows CRUD operations for managing tasks. Each task has an auto-incrementing ID, title, description, and completion status.

## Features

- Create, read, update, and delete tasks
- In-memory data storage
- Filter tasks by completion status
- Comprehensive error handling
- Thread-safe operations
- Input validation

## API Endpoints

### 1. Create a Task
- **POST** `/tasks`
- **Body**: JSON object with `title` (required), `description` (required), and optional `is_completed` (boolean, defaults to false)

```json
{
  "title": "Learn Flask",
  "description": "Build a REST API with Flask",
  "is_completed": false
}
```

**Response**: Created task with auto-generated ID (Status: 201)

### 2. Get All Tasks
- **GET** `/tasks`
- **Optional Query Parameter**: `is_completed=true|false` to filter tasks by completion status

**Examples**:
- Get all tasks: `GET /tasks`
- Get completed tasks: `GET /tasks?is_completed=true`
- Get pending tasks: `GET /tasks?is_completed=false`

**Response**: Array of tasks (Status: 200)

### 3. Get Single Task
- **GET** `/tasks/<id>`
- **Path Parameter**: `id` (integer) - Task ID

**Response**: Task object (Status: 200) or error if not found (Status: 404)

### 4. Update Task
- **PUT** `/tasks/<id>`
- **Path Parameter**: `id` (integer) - Task ID
- **Body**: JSON object with `title`, `description`, and/or `is_completed`

```json
{
  "title": "Updated title",
  "description": "Updated description",
  "is_completed": true
}
```

**Response**: Updated task object (Status: 200) or error if not found (Status: 404)

### 5. Delete Task
- **DELETE** `/tasks/<id>`
- **Path Parameter**: `id` (integer) - Task ID

**Response**: Success message (Status: 200) or error if not found (Status: 404)

### 6. Health Check
- **GET** `/health`
- **Response**: API status information including task count (Status: 200)

### 7. API Information  
- **GET** `/`
- **Response**: API information and available endpoints (Status: 200)

## Task Object Structure

```json
{
  "id": 1,
  "title": "Sample Task",
  "description": "This is a sample task",
  "is_completed": false
}
```

## Error Handling

The API includes comprehensive error handling:

- **400 Bad Request**: Invalid input data or missing required fields
- **404 Not Found**: Task not found or invalid endpoint
- **405 Method Not Allowed**: HTTP method not supported for endpoint
- **500 Internal Server Error**: Server-side errors

Error responses follow this format:
```json
{
  "error": "Error description"
}
```

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation and Setup

### Quick Setup (Recommended)

Run the automated setup script:

```bash
python setup.py
```

This script will:
- Check Python version compatibility
- Create a virtual environment
- Install all dependencies
- Provide next steps

### Manual Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Backend
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv task_api_env
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     task_api_env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source task_api_env/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **The API will be available at**
   ```
   http://localhost:5000
   ```

3. **Verify the API is running**
   - Open your browser and visit: `http://localhost:5000/health`
   - View API information: `http://localhost:5000/`
   - Or use curl: `curl http://localhost:5000/health`

## Environment Configuration

You can customize the application behavior using environment variables:

```bash
# Set environment (development, production, testing)
set FLASK_ENV=development

# Set custom host and port
set FLASK_HOST=127.0.0.1
set FLASK_PORT=8000

# Set secret key for production
set SECRET_KEY=your-production-secret-key

# Run with custom settings
python app.py
```

## Testing the API

You can test the API using various tools. See **`API_TESTING_GUIDE.md`** for comprehensive testing instructions.

### Quick Testing

Run the automated test script:
```bash
python test_api.py
```

### Using curl

1. **Create a task**
   ```bash
   curl -X POST http://localhost:5000/tasks \
     -H "Content-Type: application/json" \
     -d '{"title": "Learn Flask", "description": "Build a REST API"}'
   ```

2. **Get all tasks**
   ```bash
   curl http://localhost:5000/tasks
   ```

3. **Get a specific task**
   ```bash
   curl http://localhost:5000/tasks/1
   ```

4. **Update a task**
   ```bash
   curl -X PUT http://localhost:5000/tasks/1 \
     -H "Content-Type: application/json" \
     -d '{"title": "Updated Task", "description": "Updated description", "is_completed": true}'
   ```

5. **Filter completed tasks**
   ```bash
   curl http://localhost:5000/tasks?is_completed=true
   ```

6. **Delete a task**
   ```bash
   curl -X DELETE http://localhost:5000/tasks/1
   ```

### Using Postman

**📖 [View Complete Postman Documentation](https://documenter.getpostman.com/view/38560967/2sB34cohpk)**

**Option 1: Import Collection File**
1. Open Postman
2. Click "Import" → "Upload Files"
3. Select `Task_Management_API.postman_collection.json`
4. The collection will be imported with all endpoints ready to test

**Option 2: Manual Setup**
1. Create a new environment with variable `base_url` = `http://localhost:5000`
2. Import the following endpoints:
   - POST `{{base_url}}/tasks`
   - GET `{{base_url}}/tasks`
   - GET `{{base_url}}/tasks/1`
   - PUT `{{base_url}}/tasks/1`
   - DELETE `{{base_url}}/tasks/1`

3. Set the `Content-Type` header to `application/json` for POST and PUT requests

### Using Python requests

```python
import requests
import json

base_url = "http://localhost:5000"

# Create a task
task_data = {
    "title": "Test Task",
    "description": "This is a test task"
}
response = requests.post(f"{base_url}/tasks", json=task_data)
print(response.json())

# Get all tasks
response = requests.get(f"{base_url}/tasks")
print(response.json())
```

## Project Structure

```
Backend/
├── app.py                                      # Main Flask application entry point
├── requirements.txt                            # Python dependencies
├── test_api.py                                 # API testing script
├── API_TESTING_GUIDE.md                        # Comprehensive testing guide
├── Task_Management_API.postman_collection.json # Postman collection file
├── .gitignore                                  # Git ignore file
├── README.md                                   # This file
├── config/                                     # Configuration files
│   ├── __init__.py
│   └── config.py                               # App configuration settings
├── models/                                     # Data models
│   ├── __init__.py
│   └── task.py                                 # Task model and TaskManager
├── controllers/                                # Business logic controllers
│   ├── __init__.py
│   └── task_controller.py                      # Task-related business logic
└── routes/                                     # API route definitions
    ├── __init__.py
    ├── task_routes.py                          # Task-related routes
    └── general_routes.py                       # General routes (health, info)
```

## Architecture

The application follows a clean architecture pattern with separation of concerns:

- **Routes**: Handle HTTP requests and responses, parameter extraction
- **Controllers**: Contain business logic and coordinate between routes and models
- **Models**: Handle data operations and business entities
- **Config**: Application configuration and environment settings

### Benefits of this Structure:

1. **Maintainability**: Each component has a single responsibility
2. **Scalability**: Easy to add new features without affecting existing code
3. **Testability**: Controllers and models can be tested independently
4. **Readability**: Clear separation makes the code easier to understand
5. **Reusability**: Controllers can be used by different route handlers

## Development Notes

- The API uses in-memory storage, so data will be lost when the server restarts
- The server runs in debug mode for development (change FLASK_ENV=production for production)
- Thread-safe operations are implemented using Python's threading.Lock
- Input validation ensures data integrity
- Auto-incrementing IDs are thread-safe
- The application follows MVC (Model-View-Controller) architecture pattern
- Configuration is environment-based and can be customized via environment variables
- Blueprints are used for better route organization

## Future Enhancements

- Add database persistence (SQLite, PostgreSQL, etc.)
- Implement authentication and authorization
- Add pagination for large datasets
- Add more sophisticated filtering and sorting
- Add task categories or tags
- Add due dates and priority levels
- Implement task search functionality

## License

This project is open source and available under the MIT License.
