import os


class Config:
    DEBUG = os.getenv('DEBUG', False)
    PORT = os.getenv('PORT')
    HOST = os.getenv('HOST')
    COLLECTION_EXERCISE_URL = os.getenv('COLLECTION_EXERCISE_URL')
    SURVEY_URL = os.getenv('SURVEY_URL')
    REPORTING_URL = os.getenv('REPORTING_URL')
    AUTH_USERNAME = os.getenv('AUTH_USERNAME')
    AUTH_PASSWORD = os.getenv('AUTH_PASSWORD')
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO')


class DevelopmentConfig(Config):
    DEBUG = os.getenv('DEBUG', True)
    PORT = os.getenv('PORT', 5000)
    HOST = os.getenv('HOST', 'localhost')
    ENV = os.getenv('FLASK_ENV', 'development')
    COLLECTION_EXERCISE_URL = os.getenv('COLLECTION_EXERCISE_URL', 'http://localhost:8145/')
    SURVEY_URL = os.getenv('SURVEY_URL', 'http://localhost:8080/')
    REPORTING_URL = os.getenv('REPORTING_URL', 'http://localhost:8084/')
    AUTH_USERNAME = os.getenv('AUTH_USERNAME', 'admin')
    AUTH_PASSWORD = os.getenv('AUTH_PASSWORD', 'secret')


class TestingConfig(DevelopmentConfig):
    PORT = os.getenv('PORT', 5000)
    HOST = os.getenv('HOST', 'localhost')
    TESTING = True
