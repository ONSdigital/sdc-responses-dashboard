import unittest

from app.setup import create_app
from config import TestingConfig


class AppContextTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config.from_object(TestingConfig)
        self.test_client = self.app.test_client()
