import json
import os

import responses

from app.exceptions import UnknownSurveyError
from app.survey_metadata import (
    fetch_survey_and_collection_exercise_metadata,
    get_event_timestamp_for_tag,
    map_collection_exercise_id_to_survey_id,
    map_surveys_to_collection_exercises,
)
from tests.app import AppContextTestCase


class TestSurveyMetadata(AppContextTestCase):
    this_file_path = os.path.dirname(__file__)

    with open(os.path.join(this_file_path, "../test_data/get_surveys_response.json")) as fp:
        surveys_response = json.load(fp)

    with open(os.path.join(this_file_path, "../test_data/get_collection_exercises_response.json")) as fp:
        collection_exercises_response = json.load(fp)

    def test_map_surveys_to_collection_exercises(self):
        expected_result = [
            {
                "surveyId": "cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87",
                "shortName": "BRES",
                "surveyType": "Business",
                "longName": "Business Register and Employment Survey",
                "surveyRef": "221",
                "collectionExercises": [
                    {
                        "collectionExerciseId": "14fb3e68-4dca-46db-bf49-04b84e07e77c",
                        "userDescription": "December 2017",
                        "exerciseRef": "201712",
                        "exerciseGoLiveDate": "2017-09-11T24:00:00.000Z",
                        "exerciseReturnDate": "2017-10-06T00:00:00.000Z",
                    },
                    {
                        "collectionExerciseId": "24fb3e68-4dca-46db-bf49-04b84e07e77c",
                        "userDescription": "January 2018",
                        "exerciseRef": "201801",
                        "exerciseGoLiveDate": "2017-09-11T24:00:00.000Z",
                        "exerciseReturnDate": "2017-10-06T00:00:00.000Z",
                    },
                ],
            },
            {
                "surveyId": "04dbb407-4438-4f89-acc4-53445d753111",
                "shortName": "QBS",
                "surveyType": "Business",
                "longName": "Quarterly Business Survey",
                "surveyRef": "064",
                "collectionExercises": [
                    {
                        "collectionExerciseId": "14fb3e68-4dca-46db-bf49-04b84e07e777",
                        "userDescription": "Quarterly Business Survey",
                        "exerciseRef": "201812",
                        "exerciseGoLiveDate": "2017-09-11T24:00:00.000Z",
                        "exerciseReturnDate": "2017-10-06T00:00:00.000Z",
                    }
                ],
            },
        ]

        actual_result = map_surveys_to_collection_exercises(self.surveys_response, self.collection_exercises_response)

        self.assertEqual(expected_result, actual_result)

    def test_map_collection_exercise_id_to_survey_id(self):
        expected_result = {
            "14fb3e68-4dca-46db-bf49-04b84e07e777": {
                "exerciseRef": "201812",
                "longName": "Quarterly Business Survey",
                "shortName": "QBS",
                "surveyId": "04dbb407-4438-4f89-acc4-53445d753111",
                "surveyType": "Business",
                "userDescription": "Quarterly Business Survey",
                "exerciseGoLiveDate": "2017-09-11T24:00:00.000Z",
                "exerciseReturnDate": "2017-10-06T00:00:00.000Z",
            },
            "14fb3e68-4dca-46db-bf49-04b84e07e77c": {
                "exerciseRef": "201712",
                "longName": "Business Register and Employment Survey",
                "shortName": "BRES",
                "surveyId": "cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87",
                "surveyType": "Business",
                "userDescription": "December 2017",
                "exerciseReturnDate": "2017-10-06T00:00:00.000Z",
                "exerciseGoLiveDate": "2017-09-11T24:00:00.000Z",
            },
            "24fb3e68-4dca-46db-bf49-04b84e07e77c": {
                "exerciseRef": "201801",
                "longName": "Business Register and Employment Survey",
                "shortName": "BRES",
                "surveyId": "cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87",
                "surveyType": "Business",
                "userDescription": "January 2018",
                "exerciseGoLiveDate": "2017-09-11T24:00:00.000Z",
                "exerciseReturnDate": "2017-10-06T00:00:00.000Z",
            },
        }

        actual_result = map_collection_exercise_id_to_survey_id(
            map_surveys_to_collection_exercises(self.surveys_response, self.collection_exercises_response)
        )

        self.assertEqual(expected_result, actual_result)

    def test_unknown_survey_id_raises_unknown_survey_exception(self):
        with self.assertRaises(UnknownSurveyError) as e:
            map_surveys_to_collection_exercises({}, self.collection_exercises_response)
            self.assertEqual(e.survey_id, "cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87")

    @responses.activate
    def test_only_ready_business_collection_exercises_returned_after_filter(self):
        collection_exercises, surveys = self.fetch_mock_survey_and_collection_exercises_response()

        expected_surveys = [
            {
                "surveyId": "cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87",
                "shortName": "BRES",
                "longName": "Business Register and Employment Survey",
                "surveyRef": "221",
                "surveyType": "Business",
                "collectionExercises": [
                    {
                        "collectionExerciseId": "24fb3e68-4dca-46db-bf49-04b84e07e77c",
                        "userDescription": "January 2018",
                        "exerciseRef": "201801",
                        "exerciseGoLiveDate": "2017-09-11T24:00:00.000Z",
                        "exerciseReturnDate": "2017-10-06T00:00:00.000Z",
                    }
                ],
            },
            {
                "surveyId": "04dbb407-4438-4f89-acc4-53445d753111",
                "shortName": "QBS",
                "longName": "Quarterly Business Survey",
                "surveyRef": "064",
                "surveyType": "Business",
                "collectionExercises": [
                    {
                        "collectionExerciseId": "14fb3e68-4dca-46db-bf49-04b84e07e777",
                        "userDescription": "Quarterly Business Survey",
                        "exerciseRef": "201812",
                        "exerciseGoLiveDate": "2017-09-11T24:00:00.000Z",
                        "exerciseReturnDate": "2017-10-06T00:00:00.000Z",
                    }
                ],
            },
        ]

        expected_collection_exercises = {
            "14fb3e68-4dca-46db-bf49-04b84e07e777": {
                "exerciseRef": "201812",
                "longName": "Quarterly Business Survey",
                "shortName": "QBS",
                "surveyType": "Business",
                "surveyId": "04dbb407-4438-4f89-acc4-53445d753111",
                "userDescription": "Quarterly Business Survey",
                "exerciseGoLiveDate": "2017-09-11T24:00:00.000Z",
                "exerciseReturnDate": "2017-10-06T00:00:00.000Z",
            },
            "24fb3e68-4dca-46db-bf49-04b84e07e77c": {
                "exerciseRef": "201801",
                "longName": "Business Register and Employment Survey",
                "shortName": "BRES",
                "surveyType": "Business",
                "surveyId": "cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87",
                "userDescription": "January 2018",
                "exerciseGoLiveDate": "2017-09-11T24:00:00.000Z",
                "exerciseReturnDate": "2017-10-06T00:00:00.000Z",
            },
        }

        self.assertEqual(expected_surveys, surveys, "Filtered and mapped surveys did not match expected result")

        self.assertEqual(
            expected_collection_exercises,
            collection_exercises,
            "Filtered and mapped collection exercises did not match expected result",
        )

    @responses.activate
    def test_only_business_surveys_are_returned_by_fetch(self):
        collection_exercises, surveys = self.fetch_mock_survey_and_collection_exercises_response()

        for survey in surveys:
            self.assertEqual(
                survey["surveyType"],
                "Business",
                'Found survey type not equal to "Business" in surveys list',
            )

        for collection_exercise in collection_exercises.values():
            self.assertEqual(
                collection_exercise["surveyType"],
                "Business",
                'Found survey type not equal to "Business" in collection exercise map',
            )

    def test_get_event_timestamp_for_tag(self):
        timestamp = "2017-09-11T24:00:00.000Z"
        event_timestamp = get_event_timestamp_for_tag([{"tag": "go_live", "timestamp": timestamp}], "go_live")
        self.assertEqual(event_timestamp, timestamp)

    def test_get_event_timestamp_for_tag_missing_event(self):
        event_timestamp = get_event_timestamp_for_tag(
            [{"tag": "return_by", "timestamp": "2017-10-11T24:00:00.000Z"}], "go_live"
        )
        self.assertEqual(event_timestamp, None)

    def test_get_event_timestamp_for_tag_empty_events(self):
        event_timestamp = get_event_timestamp_for_tag({}, "go_live")
        self.assertEqual(event_timestamp, None)

    def test_get_event_timestamp_for_tag_none_events(self):
        event_timestamp = get_event_timestamp_for_tag(None, "go_live")
        self.assertEqual(event_timestamp, None)

    def fetch_mock_survey_and_collection_exercises_response(self):
        # Requires @responses.activate
        with self.app.app_context():
            # Mock the survey and collection exercise services
            responses.add(
                responses.GET,
                self.app.config["SURVEY_URL"] + "/surveys",
                json=self.surveys_response,
            )
            responses.add(
                responses.GET,
                self.app.config["COLLECTION_EXERCISE_URL"] + "/collectionexercises",
                json=self.collection_exercises_response,
            )

            surveys, collection_exercises = fetch_survey_and_collection_exercise_metadata()
        return collection_exercises, surveys
