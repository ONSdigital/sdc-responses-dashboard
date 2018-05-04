import os


class Config:
    DEBUG = os.getenv('DEBUG', False)
    PORT = os.getenv('PORT')
    HOST = os.getenv('HOST')


class DevelopmentConfig(Config):
    DEBUG = os.getenv('DEBUG', True)
    PORT = os.getenv('PORT', 5000)
    HOST = os.getenv('HOST', 'localhost')
    ENV = os.getenv('FLASK_ENV', 'development')


class TestingConfig(Config):
    PORT = os.getenv('PORT', 5000)
    HOST = os.getenv('HOST', 'localhost')
    TESTING = True
