import json
import os
import unittest

from app.common.survey_metadata import map_surveys_to_collection_exercises, map_collection_exercise_id_to_survey_id
from app.exceptions import UnknownSurveyError


class TestSurveyMetadata(unittest.TestCase):

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
                'surveyRef': '221',
                'collectionExercises': [
                    {
                        'collexId': '14fb3e68-4dca-46db-bf49-04b84e07e77c',
                        'collexName': 'BRES_2017'
                    }
                ]
            },
            {
                'surveyId': '04dbb407-4438-4f89-acc4-53445d75330c',
                'shortName': 'AOFDI',
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
                'collexName': 'BRES_2017'
            }
        }

        actual_result = map_collection_exercise_id_to_survey_id(
            map_surveys_to_collection_exercises(self.surveys_response, self.collection_exercises_response))

        self.assertEqual(expected_result, actual_result)

    def test_unknown_survey_id_raises_unknown_survey_exception(self):
        with self.assertRaises(UnknownSurveyError) as e:
            map_surveys_to_collection_exercises({}, self.collection_exercises_response)
            self.assertEqual(e.survey_id, 'cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87')
