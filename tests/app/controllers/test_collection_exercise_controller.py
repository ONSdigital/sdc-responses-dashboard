import json
import os

from requests import HTTPError
import responses

from app.controllers.collection_exercise_controller import get_collection_exercise_list
from tests.app import AppContextTestCase


class TestSurveyController(AppContextTestCase):
    this_file_path = os.path.dirname(__file__)

    with open(os.path.join(this_file_path, '../../test_data/get_collection_exercises_response.json')) as fp:
        collection_exercises_response = json.load(fp)

    @responses.activate
    def test_get_collection_exercise_list_success(self):
        with self.app.app_context():
            responses.add(
                responses.GET,
                self.app.config['COLLECTION_EXERCISE_URL'] + 'collectionexercises',
                json=self.collection_exercises_response,
                status=200)

            controller_output = get_collection_exercise_list()

        self.assertEqual(self.collection_exercises_response, controller_output)

    @responses.activate
    def test_get_collection_exercise_list_auth_failure_raises_http_error(self):
        with self.app.app_context():
            responses.add(
                responses.GET,
                self.app.config['COLLECTION_EXERCISE_URL'] + 'collectionexercises',
                status=401)

            with self.assertRaises(HTTPError):
                get_collection_exercise_list()
