import json
import os

import responses

from app.common.survey_metadata import map_surveys_to_collection_exercises, map_collection_exercise_id_to_survey_id, \
    fetch_survey_and_collection_exercise_metadata
from app.exceptions import UnknownSurveyError
from tests.app import AppContextTestCase


class TestSurveyMetadata(AppContextTestCase):
    this_file_path = os.path.dirname(__file__)

    with open(os.path.join(this_file_path, '../../test_data/get_surveys_response.json')) as fp:
        surveys_response = json.load(fp)

    with open(os.path.join(this_file_path, '../../test_data/get_collection_exercises_response.json')) as fp:
        collection_exercises_response = json.load(fp)

    def test_map_surveys_to_collection_exercises(self):
        expected_result = [
            {
                'surveyId': 'cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87',
                'shortName': 'BRES',
                'longName': 'Business Register and Employment Survey',
                'surveyRef': '221',
                'collectionExercises': [
                    {
                        'collectionExerciseId': '14fb3e68-4dca-46db-bf49-04b84e07e77c',
                        'userDescription': 'December 2017',
                        'exerciseRef': '201712'
                    },
                    {
                        'collectionExerciseId': '24fb3e68-4dca-46db-bf49-04b84e07e77c',
                        'userDescription': 'January 2018',
                        'exerciseRef': '201801'
                    }
                ]
            },
            {
                'surveyId': '04dbb407-4438-4f89-acc4-53445d75330c',
                'shortName': 'AOFDI',
                'longName': 'Annual Outward Foreign Direct Investment Survey',
                'surveyRef': '063',
                'collectionExercises': []
            }
        ]

        actual_result = map_surveys_to_collection_exercises(
            self.surveys_response,
            self.collection_exercises_response)

        self.assertEqual(expected_result, actual_result)

    def test_map_collection_exercise_id_to_survey_id(self):
        expected_result = {
            '14fb3e68-4dca-46db-bf49-04b84e07e77c': {
                'surveyId': 'cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87',
                'shortName': 'BRES',
                'longName': 'Business Register and Employment Survey',
                'userDescription': 'December 2017',
                'exerciseRef': '201712'
            },
            '24fb3e68-4dca-46db-bf49-04b84e07e77c': {
                'surveyId': 'cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87',
                'shortName': 'BRES',
                'longName': 'Business Register and Employment Survey',
                'userDescription': 'January 2018',
                'exerciseRef': '201801'
            }
        }

        actual_result = map_collection_exercise_id_to_survey_id(
            map_surveys_to_collection_exercises(self.surveys_response, self.collection_exercises_response))

        self.assertEqual(expected_result, actual_result)

    def test_unknown_survey_id_raises_unknown_survey_exception(self):
        with self.assertRaises(UnknownSurveyError) as e:
            map_surveys_to_collection_exercises({}, self.collection_exercises_response)
            self.assertEqual(e.survey_id, 'cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87')

    @responses.activate
    def test_only_ready_collection_exercises_returned_after_filter(self):

        with self.app.app_context():

            # Mock the survey and collection exercise services
            responses.add(
                responses.GET,
                self.app.config['SURVEY_URL'] + 'surveys',
                json=self.surveys_response)
            responses.add(
                responses.GET,
                self.app.config['COLLECTION_EXERCISE_URL'] + 'collectionexercises',
                json=self.collection_exercises_response)

            surveys, collection_exercises = fetch_survey_and_collection_exercise_metadata()

        expected_surveys = [
            {
                'surveyId': 'cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87',
                'shortName': 'BRES',
                'longName': 'Business Register and Employment Survey',
                'surveyRef': '221',
                'collectionExercises': [
                    {
                        'collectionExerciseId': '24fb3e68-4dca-46db-bf49-04b84e07e77c',
                        'userDescription': 'January 2018',
                        'exerciseRef': '201801'
                    }
                ]
            },
            {
                'surveyId': '04dbb407-4438-4f89-acc4-53445d75330c',
                'shortName': 'AOFDI',
                'longName': 'Annual Outward Foreign Direct Investment Survey',
                'surveyRef': '063',
                'collectionExercises': []
            }
        ]

        expected_collection_exercises = {
            '24fb3e68-4dca-46db-bf49-04b84e07e77c': {
                'surveyId': 'cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87',
                'shortName': 'BRES',
                'longName': 'Business Register and Employment Survey',
                'userDescription': 'January 2018',
                'exerciseRef': '201801'
            }
        }

        self.assertEqual(expected_surveys,
                         surveys,
                         'Filtered and mapped surveys did not match expected result')

        self.assertEqual(expected_collection_exercises,
                         collection_exercises,
                         'Filtered and mapped collection exercises did not match expected result')
