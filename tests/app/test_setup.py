import unittest

from app.exceptions import MissingConfigError
from app.setup import check_required_config
from config import DevelopmentConfig


class TestSetup(unittest.TestCase):
    def test_incomplete_config_raises_exception(self):
        class IncompleteConfig:
            HOST = "TEST"

        with self.assertRaises(MissingConfigError) as exception_context:
            check_required_config(IncompleteConfig)

        self.assertIn(
            "PORT", exception_context.exception.keys, msg='"PORT" variable which is missing is not present in exception'
        )
        self.assertNotIn(
            "HOST", exception_context.exception.keys, msg='"HOST" variable in exception even though HOST should be set'
        )

    def test_empty_string_in_config_raises_exception(self):
        class IncompleteConfig:
            HOST = ""

        with self.assertRaises(MissingConfigError) as exception_context:
            check_required_config(IncompleteConfig)

        self.assertIn(
            "HOST", exception_context.exception.keys, msg='"HOST" variable which is missing is not present in exception'
        )

    @staticmethod
    def test_development_config_successfully_checked():
        check_required_config(DevelopmentConfig)
