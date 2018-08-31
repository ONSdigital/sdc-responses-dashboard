from distutils.util import strtobool
import os

REQUIRED_ENVIRONMENT_VARIABLES = {
    'PORT',
    'HOST',
    'COLLECTION_EXERCISE_URL',
    'SURVEY_URL',
    'REPORTING_URL',
    'REPORTING_REFRESH_CYCLE',
    'AUTH_USERNAME',
    'AUTH_PASSWORD'
}


class Config:
    DEBUG = os.getenv('DEBUG', False)
    PORT = os.getenv('PORT')
    HOST = os.getenv('HOST')
    COLLECTION_EXERCISE_URL = os.getenv('COLLECTION_EXERCISE_URL')
    SURVEY_URL = os.getenv('SURVEY_URL')
    REPORTING_URL = os.getenv('REPORTING_URL')
    REPORTING_REFRESH_CYCLE = os.getenv('REPORTING_REFRESH_CYCLE')
    AUTH_USERNAME = os.getenv('AUTH_USERNAME')
    AUTH_PASSWORD = os.getenv('AUTH_PASSWORD')
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO')
    LOGGING_JSON_INDENT = os.getenv('LOGGING_JSON_INDENT')


class DevelopmentConfig(Config):
    DEBUG = os.getenv('DEBUG', True)
    PORT = os.getenv('PORT', '5000')
    HOST = os.getenv('HOST', 'localhost')
    ENV = os.getenv('FLASK_ENV', 'development')
    COLLECTION_EXERCISE_URL = os.getenv('COLLECTION_EXERCISE_URL', 'http://localhost:8145/')
    SURVEY_URL = os.getenv('SURVEY_URL', 'http://localhost:8080/')
    REPORTING_URL = os.getenv('REPORTING_URL', 'http://localhost:8084/')
    REPORTING_REFRESH_CYCLE = os.getenv('REPORTING_REFRESH_CYCLE', '10000')
    AUTH_USERNAME = os.getenv('AUTH_USERNAME', 'admin')
    AUTH_PASSWORD = os.getenv('AUTH_PASSWORD', 'secret')
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'DEBUG')
    LOGGING_JSON_INDENT = os.getenv('LOGGING_JSON_INDENT', '4')


class TestingConfig(Config):
    testing_url = 'http://test/'
    COLLECTION_EXERCISE_URL = testing_url
    SURVEY_URL = testing_url
    REPORTING_URL = testing_url
    PORT = '5000'
    HOST = 'localhost'
    TESTING = True
    ENV = 'testing'
    REPORTING_REFRESH_CYCLE = '10000'
    AUTH_USERNAME = 'admin'
    AUTH_PASSWORD = 'secret'
