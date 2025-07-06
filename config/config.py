"""
Configuration settings for the Task Management API
"""

import os


class Config:
    """Base configuration class"""
    
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    DEBUG = os.environ.get('FLASK_DEBUG') or True
    HOST = os.environ.get('FLASK_HOST') or '0.0.0.0'
    PORT = int(os.environ.get('FLASK_PORT') or 5000)
    
    # API configuration
    API_TITLE = "Task Management API"
    API_VERSION = "1.0.0"
    API_DESCRIPTION = "A simple REST API for managing tasks"
    
    # CORS configuration
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*').split(',')
    
    # Pagination
    DEFAULT_PAGE_SIZE = 20
    MAX_PAGE_SIZE = 100


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
