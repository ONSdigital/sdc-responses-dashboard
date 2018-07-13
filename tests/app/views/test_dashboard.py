import json
import os

import responses

from tests.app import AppContextTestCase


class TestSurveyController(AppContextTestCase):
    current_file_path = os.path.dirname(__file__)

    with open(os.path.join(current_file_path, '../../test_data/get_surveys_response.json')) as fp:
        surveys_response = json.load(fp)

    with open(os.path.join(current_file_path, '../../test_data/get_collection_exercises_response.json')) as fp:
        collex_response = json.load(fp)

    def mock_successful_external_api_calls(self):
        with self.app.app_context():

            responses.add(
                responses.GET,
                self.app.config['SURVEY_URL'] + 'surveys',
                json=self.surveys_response,
                status=200)

            responses.add(
                responses.GET,
                self.app.config['COLLECTION_EXERCISE_URL'] + 'collectionexercises',
                json=self.collex_response,
                status=200)

    @responses.activate
    def test_dashboard_homepage(self):
        self.mock_successful_external_api_calls()

        response = self.test_client.get('/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Choose A Survey', response.data)
        self.assertIn(b'Survey', response.data)
        self.assertIn(b'Reference', response.data)
        self.assertIn(b'BRES', response.data)
        self.assertIn(b'Business Register and Employment Survey', response.data)
        self.assertIn(b'AOFDI', response.data)
        self.assertIn(b'Annual Outward Foreign Direct Investment Survey', response.data)

    @responses.activate
    def test_dashboard_report_fails_gracefully(self):
        self.mock_successful_external_api_calls()

        response = self.test_client.get('/dashboard/collection-exercise/24fb3e68-4dca-46db-bf49-04b84e07e77c')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'BRES | January 2018', response.data)
        self.assertIn(b'Business Register and Employment Survey', response.data)
        self.assertIn(b'Sorry, data retrieval failed', response.data)

    @responses.activate
    def test_dashboard_report_invalid_collex(self):
        self.mock_successful_external_api_calls()

        response = self.test_client.get('/dashboard/collection-exercise/invalid-collex')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Sorry, we could not find the page you were looking for.', response.data)

    @responses.activate
    def test_dashboard_redirects_to_non_trailing_slash(self):
        self.mock_successful_external_api_calls()

        response = self.test_client.get('/dashboard/')
        self.assertEqual(response.status_code, 302)
