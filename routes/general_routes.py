"""
General routes for the Task Management API
"""

from flask import Blueprint, jsonify
from controllers.task_controller import task_controller

# Create blueprint for general routes
general_bp = Blueprint('general', __name__)


@general_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    result, status_code = task_controller.get_health_status()
    return jsonify(result), status_code


@general_bp.route('/', methods=['GET'])
def api_info():
    """API information endpoint"""
    return jsonify({
        'name': 'Task Management API',
        'version': '1.0.0',
        'description': 'A simple REST API for managing tasks',
        'endpoints': {
            'health': '/health',
            'tasks': {
                'create': 'POST /tasks',
                'get_all': 'GET /tasks',
                'get_by_id': 'GET /tasks/<id>',
                'update': 'PUT /tasks/<id>',
                'delete': 'DELETE /tasks/<id>',
                'filter': 'GET /tasks?is_completed=true|false'
            }
        }
    }), 200
