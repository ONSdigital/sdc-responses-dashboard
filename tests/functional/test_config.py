import os


class TestConfig:
    DASHBOARD_URL = os.getenv("DASHBOARD_URL", "http://localhost:8078")
    AUTH_USERNAME = os.getenv("AUTH_USERNAME", "admin")
    AUTH_PASSWORD = os.getenv("AUTH_PASSWORD", "secret")
