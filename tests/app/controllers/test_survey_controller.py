import json
import os

import responses

from app.controllers.survey_controller import get_survey_list
from tests.app.app_context_test_case import AppContextTestCase


class TestSurveyController(AppContextTestCase):
    this_file_path = os.path.dirname(__file__)

    with open(os.path.join(this_file_path, '../../test_data/get_surveys_response.json')) as fp:
        surveys_response = json.load(fp)

    @responses.activate
    def test_get_survey_list_success(self):
        with self.app.app_context():
            responses.add(
                responses.GET,
                self.app.config['SURVEY_URL'] + 'surveys',
                json=self.surveys_response,
                status=200)

            controller_output = get_survey_list()

        self.assertEqual(self.surveys_response, controller_output)
