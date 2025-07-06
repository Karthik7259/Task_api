# Task Management REST API

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A robust, lightweight REST API built with Flask for efficient task management. Features comprehensive CRUD operations, thread-safe in-memory storage, and extensive error handling.

## 🚀 Features

- **Full CRUD Operations**: Create, read, update, and delete tasks
- **Thread-Safe**: Concurrent request handling with proper synchronization
- **Input Validation**: Comprehensive data validation and sanitization
- **Error Handling**: Detailed error responses with appropriate HTTP status codes
- **Filtering**: Query tasks by completion status
- **Clean Architecture**: MVC pattern with separation of concerns
- **RESTful Design**: Follows REST API best practices

## 📋 Table of Contents

- [Quick Start](#️-quick-start)
- [API Documentation](#-api-documentation)
- [Installation](#️-installation)
- [Usage Examples](#-usage-examples)
- [Testing](#-testing)
- [Architecture](#️-architecture)
- [Configuration](#️-configuration)
- [Deployment](#-deployment)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)
- [📖 Postman Documentation](https://documenter.getpostman.com/view/38560967/2sB34cohpk)

## 🏃‍♂️ Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd task-management-api
   ```

2. **Run the automated setup**
   ```bash
   python setup.py
   ```

3. **Start the server**
   ```bash
   python app.py
   ```

4. **Verify installation**
   ```bash
   curl http://localhost:5000/health
   ```

The API will be available at `http://localhost:5000`

## 📚 API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

| Method | Endpoint | Description | Status Codes |
|--------|----------|-------------|--------------|
| GET | `/` | API information | 200 |
| GET | `/health` | Health check | 200 |
| POST | `/tasks` | Create a task | 201, 400 |
| GET | `/tasks` | Get all tasks | 200 |
| GET | `/tasks/<id>` | Get specific task | 200, 404 |
| PUT | `/tasks/<id>` | Update task | 200, 400, 404 |
| DELETE | `/tasks/<id>` | Delete task | 200, 404 |

### Data Models

#### Task Object
```json
{
  "id": 1,
  "title": "Sample Task",
  "description": "Task description",
  "is_completed": false
}
```

#### Request/Response Examples

**Create Task**
```bash
POST /tasks
Content-Type: application/json

{
  "title": "Learn Flask",
  "description": "Build a REST API with Flask",
  "is_completed": false
}
```

**Filter Tasks**
```bash
GET /tasks?is_completed=true
```

**Update Task**
```bash
PUT /tasks/1
Content-Type: application/json

{
  "title": "Updated Task",
  "is_completed": true
}
```

### Error Handling

All error responses follow this format:
```json
{
  "error": "Error description"
}
```

**HTTP Status Codes**
- `200` - Success
- `201` - Created
- `400` - Bad Request (validation error)
- `404` - Not Found
- `405` - Method Not Allowed
- `500` - Internal Server Error

## 🛠️ Installation

### Automated Setup (Recommended)

```bash
python setup.py
```

### Manual Setup

1. **Create virtual environment**
   ```bash
   python -m venv task_api_env
   ```

2. **Activate virtual environment**
   ```bash
   # Windows
   task_api_env\Scripts\activate
   
   # macOS/Linux
   source task_api_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

## 💻 Usage Examples

### Python Requests

```python
import requests

base_url = "http://localhost:5000"

# Create a task
task_data = {
    "title": "Complete Project",
    "description": "Finish the Flask API project"
}
response = requests.post(f"{base_url}/tasks", json=task_data)
task = response.json()

# Get all tasks
response = requests.get(f"{base_url}/tasks")
tasks = response.json()

# Update task
update_data = {"is_completed": True}
response = requests.put(f"{base_url}/tasks/{task['id']}", json=update_data)
```

### cURL Examples

```bash
# Create task
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "New Task", "description": "Task description"}'

# Get all tasks
curl http://localhost:5000/tasks

# Get completed tasks only
curl "http://localhost:5000/tasks?is_completed=true"

# Update task
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"is_completed": true}'

# Delete task
curl -X DELETE http://localhost:5000/tasks/1
```

### Postman Collection

Import the provided Postman collection for easy testing:

**📖 [Complete Postman Documentation](https://documenter.getpostman.com/view/38560967/2sB34cohpk)**

1. Open Postman
2. Click "Import" → "Upload Files"
3. Select `Task_Management_API.postman_collection.json`

## 🧪 Testing

### Automated Testing

Run the comprehensive test suite:
```bash
python test_api.py
```

### Manual Testing

See `API_TESTING_GUIDE.md` for detailed testing instructions and examples.

## 🏗️ Architecture

The application follows a clean MVC architecture pattern:

```
Backend/
├── app.py                    # Application entry point
├── requirements.txt          # Dependencies
├── config/
│   └── config.py            # Configuration settings
├── models/
│   └── task.py              # Data models and business logic
├── controllers/
│   └── task_controller.py   # Business logic controllers
└── routes/
    ├── task_routes.py       # Task-related endpoints
    └── general_routes.py    # General endpoints
```

### Design Principles

- **Separation of Concerns**: Each layer has a distinct responsibility
- **Single Responsibility**: Each module focuses on one aspect
- **Dependency Injection**: Loose coupling between components
- **Thread Safety**: Safe concurrent operations
- **Input Validation**: Comprehensive data validation

## ⚙️ Configuration

### Environment Variables

```bash
# Application environment
FLASK_ENV=development          # development, production, testing

# Server configuration
FLASK_HOST=127.0.0.1          # Server host
FLASK_PORT=5000               # Server port

# Security
SECRET_KEY=your-secret-key    # Production secret key
```

### Custom Configuration

```python
# config/config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DEBUG = os.environ.get('FLASK_ENV') == 'development'
    HOST = os.environ.get('FLASK_HOST') or '127.0.0.1'
    PORT = int(os.environ.get('FLASK_PORT') or 5000)
```

## 🚀 Deployment

### Production Considerations

1. **Set production environment**
   ```bash
   export FLASK_ENV=production
   export SECRET_KEY=your-production-secret-key
   ```

2. **Use a production WSGI server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. **Enable HTTPS** in production environments

## 🔮 Future Enhancements

- [ ] Database persistence (PostgreSQL, MongoDB)
- [ ] Authentication and authorization (JWT)
- [ ] Task categories and tags
- [ ] Due dates and priority levels
- [ ] Search and advanced filtering
- [ ] Pagination for large datasets
- [ ] Rate limiting
- [ ] Caching layer
- [ ] API versioning
- [ ] Documentation with OpenAPI/Swagger

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/task-management-api.git

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Run linting
flake8 .
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Flask team for the excellent web framework
- Contributors and testers
- Open source community

---

**Built with ❤️ using Flask**

For questions or support, please open an issue or contact the maintainers.
