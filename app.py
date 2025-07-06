"""
Task Management REST API

A simple Flask REST API for managing tasks with proper project structure.
Organized with separate routes, controllers, models, and configuration.
"""

import os
from flask import Flask, jsonify

# Import configuration
from config import config

# Import routes
from routes import task_bp, general_bp


def create_app(config_name=None):
    """Application factory pattern"""
    
    # Create Flask application
    app = Flask(__name__)
    
    # Load configuration
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    
    app.config.from_object(config[config_name])
    
    # Register blueprints
    app.register_blueprint(general_bp)
    app.register_blueprint(task_bp)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Endpoint not found'}), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({'error': 'Method not allowed'}), 405

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    return app


def run_app():
    """Run the Flask application"""
    app = create_app()
    
    # Get configuration
    config_name = os.environ.get('FLASK_ENV', 'default')
    config_obj = config[config_name]
    
    # Run the application
    app.run(
        debug=config_obj.DEBUG,
        host=config_obj.HOST,
        port=config_obj.PORT
    )


if __name__ == '__main__':
    run_app()
