"""
Task model for the Task Management API
"""

from typing import Dict, List, Optional
import threading


class Task:
    """Task model class"""
    
    def __init__(self, title: str, description: str, is_completed: bool = False):
        self.id = None  # Will be set by TaskManager
        self.title = title
        self.description = description
        self.is_completed = is_completed

    def to_dict(self) -> Dict:
        """Convert task to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'is_completed': self.is_completed
        }
    
    def update(self, title: str = None, description: str = None, is_completed: bool = None):
        """Update task fields"""
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if is_completed is not None:
            self.is_completed = is_completed


class TaskManager:
    """Task manager for handling task operations"""
    
    def __init__(self):
        self.tasks: List[Dict] = []
        self.task_id_counter = 1
        self.lock = threading.Lock()
    
    def create_task(self, title: str, description: str, is_completed: bool = False) -> Dict:
        """Create a new task"""
        task = Task(title, description, is_completed)
        
        with self.lock:
            task.id = self.task_id_counter
            self.task_id_counter += 1
            task_dict = task.to_dict()
            self.tasks.append(task_dict)
            
        return task_dict
    
    def get_all_tasks(self, is_completed: Optional[bool] = None) -> List[Dict]:
        """Get all tasks with optional filtering"""
        if is_completed is not None:
            return [task for task in self.tasks if task['is_completed'] == is_completed]
        return self.tasks.copy()
    
    def get_task_by_id(self, task_id: int) -> Optional[Dict]:
        """Get a task by ID"""
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: str = None, description: str = None, 
                   is_completed: bool = None) -> Optional[Dict]:
        """Update a task by ID"""
        task = self.get_task_by_id(task_id)
        if task is None:
            return None
        
        with self.lock:
            if title is not None:
                task['title'] = title
            if description is not None:
                task['description'] = description
            if is_completed is not None:
                task['is_completed'] = is_completed
        
        return task
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID"""
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        with self.lock:
            self.tasks.remove(task)
        
        return True
    
    def get_tasks_count(self) -> int:
        """Get total number of tasks"""
        return len(self.tasks)


# Global task manager instance
task_manager = TaskManager()
