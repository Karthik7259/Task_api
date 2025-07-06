"""
Task routes for the Task Management API
"""

from flask import Blueprint, request, jsonify
from controllers.task_controller import task_controller

# Create blueprint for task routes
task_bp = Blueprint('tasks', __name__)


@task_bp.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    data = request.get_json()
    result, status_code = task_controller.create_task(data)
    return jsonify(result), status_code


@task_bp.route('/tasks', methods=['GET'])
def get_all_tasks():
    """Get all tasks with optional filtering by completion status"""
    is_completed_param = request.args.get('is_completed')
    result, status_code = task_controller.get_all_tasks(is_completed_param)
    return jsonify(result), status_code


@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id: int):
    """Get a single task by ID"""
    result, status_code = task_controller.get_task_by_id(task_id)
    return jsonify(result), status_code


@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id: int):
    """Update a task by ID"""
    data = request.get_json()
    result, status_code = task_controller.update_task(task_id, data)
    return jsonify(result), status_code


@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id: int):
    """Delete a task by ID"""
    result, status_code = task_controller.delete_task(task_id)
    return jsonify(result), status_code
