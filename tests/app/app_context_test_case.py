import unittest

from app.setup import create_app
from config import TestingConfig


class AppContextTestCase(unittest.TestCase):

    def setUp(self):
        app = create_app()
        app.config.from_object(TestingConfig)
        self.app = app
        self.test_client = app.test_client()
