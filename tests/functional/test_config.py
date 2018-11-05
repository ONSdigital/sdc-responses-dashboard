import os


class TestConfig:
    DASHBOARD_URL = os.getenv('DASHBOARD_URL', 'http://localhost:5000')
    MAX_COLLECTION_EXERCISE_RETRIES = int(os.getenv('MAX_COLLECTION_EXERCISE_RETRIES', 10))
    COLLECTION_EXERCISE_URL = os.getenv('COLLECTION_EXERCISE_URL', 'http://localhost:8145')
    AUTH_USERNAME = os.getenv('AUTH_USERNAME', 'admin')
    AUTH_PASSWORD = os.getenv('AUTH_PASSWORD', 'secret')
