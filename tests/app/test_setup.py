import unittest

from app.exceptions import MissingConfigError
from app.setup import check_required_config
from config import DevelopmentConfig


class MyTestCase(unittest.TestCase):
    def test_incomplete_config_raises_exception(self):

        class IncompleteConfig:
            HOST = 'TEST'

        with self.assertRaises(MissingConfigError) as e:
            check_required_config(IncompleteConfig)
            self.assertIn('PORT', e.keys, msg='Required variable which is missing is not present in exception')

    @staticmethod
    def test_development_config_successfully_checked():
        check_required_config(DevelopmentConfig)
