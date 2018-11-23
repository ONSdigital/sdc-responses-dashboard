import os


class TestConfig:
    DASHBOARD_URL = os.getenv('DASHBOARD_URL', 'http://localhost:5000')
    AUTH_USERNAME = os.getenv('AUTH_USERNAME', 'admin')
    AUTH_PASSWORD = os.getenv('AUTH_PASSWORD', 'secret')
