import os
import unittest

from app.setup import create_app


class AppContextTestCase(unittest.TestCase):
    def setUp(self):
        os.environ["APP_SETTINGS"] = "TestingConfig"
        self.app = create_app()
        self.test_client = self.app.test_client()
