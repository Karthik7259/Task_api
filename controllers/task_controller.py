"""
Task controller for handling task-related business logic
"""

from typing import Dict, Tuple, Union
from models.task import task_manager


class TaskController:
    """Controller class for task operations"""
    
    @staticmethod
    def validate_task_data(data: Dict) -> Tuple[bool, str]:
        """Validate task data"""
        if not data:
            return False, "Request body is required"
        
        if 'title' not in data or not data['title']:
            return False, "Title is required"
        
        if 'description' not in data:
            return False, "Description is required"
        
        if not isinstance(data['title'], str):
            return False, "Title must be a string"
        
        if not isinstance(data['description'], str):
            return False, "Description must be a string"
        
        if 'is_completed' in data and not isinstance(data['is_completed'], bool):
            return False, "is_completed must be a boolean"
        
        return True, ""
    
    @staticmethod
    def create_task(data: Dict) -> Tuple[Union[Dict, str], int]:
        """Create a new task"""
        try:
            # Validate input data
            is_valid, error_message = TaskController.validate_task_data(data)
            if not is_valid:
                return {'error': error_message}, 400
            
            # Create new task
            task = task_manager.create_task(
                title=data['title'],
                description=data['description'],
                is_completed=data.get('is_completed', False)
            )
            
            return task, 201
        
        except Exception as e:
            return {'error': 'Internal server error'}, 500
    
    @staticmethod
    def get_all_tasks(is_completed_param: str = None) -> Tuple[Union[Dict, list], int]:
        """Get all tasks with optional filtering"""
        try:
            if is_completed_param is not None:
                # Convert string to boolean
                if is_completed_param.lower() == 'true':
                    is_completed_filter = True
                elif is_completed_param.lower() == 'false':
                    is_completed_filter = False
                else:
                    return {'error': 'is_completed parameter must be true or false'}, 400
                
                # Filter tasks by completion status
                tasks = task_manager.get_all_tasks(is_completed_filter)
                return tasks, 200
            
            # Return all tasks if no filter
            tasks = task_manager.get_all_tasks()
            return tasks, 200
        
        except Exception as e:
            return {'error': 'Internal server error'}, 500
    
    @staticmethod
    def get_task_by_id(task_id: int) -> Tuple[Union[Dict, str], int]:
        """Get a single task by ID"""
        try:
            task = task_manager.get_task_by_id(task_id)
            if task is None:
                return {'error': 'Task not found'}, 404
            
            return task, 200
        
        except Exception as e:
            return {'error': 'Internal server error'}, 500
    
    @staticmethod
    def update_task(task_id: int, data: Dict) -> Tuple[Union[Dict, str], int]:
        """Update a task by ID"""
        try:
            # Check if task exists
            existing_task = task_manager.get_task_by_id(task_id)
            if existing_task is None:
                return {'error': 'Task not found'}, 404
            
            # Validate input data
            is_valid, error_message = TaskController.validate_task_data(data)
            if not is_valid:
                return {'error': error_message}, 400
            
            # Update task
            updated_task = task_manager.update_task(
                task_id=task_id,
                title=data['title'],
                description=data['description'],
                is_completed=data.get('is_completed', existing_task['is_completed'])
            )
            
            return updated_task, 200
        
        except Exception as e:
            return {'error': 'Internal server error'}, 500
    
    @staticmethod
    def delete_task(task_id: int) -> Tuple[Union[Dict, str], int]:
        """Delete a task by ID"""
        try:
            success = task_manager.delete_task(task_id)
            if not success:
                return {'error': 'Task not found'}, 404
            
            return {'message': 'Task deleted successfully'}, 200
        
        except Exception as e:
            return {'error': 'Internal server error'}, 500
    
    @staticmethod
    def get_health_status() -> Tuple[Dict, int]:
        """Get API health status"""
        try:
            task_count = task_manager.get_tasks_count()
            return {
                'status': 'healthy',
                'message': 'Task API is running',
                'tasks_count': task_count
            }, 200
        
        except Exception as e:
            return {'error': 'Internal server error'}, 500


# Create controller instance
task_controller = TaskController()
