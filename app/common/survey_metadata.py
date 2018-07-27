from structlog import get_logger

from app.controllers.collection_exercise_controller import get_collection_exercise_list
from app.controllers.survey_controller import get_survey_list
from app.exceptions import UnknownSurveyError

logger = get_logger()

SEFT_SURVEYS = {
    'cb8accda-6118-4d3b-85a3-149e28960c54',  # Bricks
    '9b6872eb-28ee-4c09-b705-c3ab1bb0f9ec',  # Blocks
    'c48d6646-eb6f-4c7c-9f37-f7b41c8d2bc6',  # Sand & Gravel
    '57a43c94-9f81-4f33-bad8-f94800a66503',  # QOFDI
    'c3eaeff3-d570-475d-9859-32c3bf87800d',  # QIFDI
    '04dbb407-4438-4f89-acc4-53445d75330c',  # AOFDI
    '41320b22-b425-4fba-a90e-718898f718ce',  # AIFDI
    '6aa8896f-ced5-4694-800c-6cd661b0c8b2',  # ASHE
    'cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87',  # BRES
    '0fc6fa22-8938-43b6-81c5-f1ccca5a5494',  # OFATS
    '7a2c9d6c-9aaf-4cf0-a68c-1d50b3f1b296',  # NBS
    '416b8a82-2031-4f41-b59b-95482d916ca3',  # PCS
    'a81f8a72-47e1-4fcf-a88b-0c175829e02b'   # GoVERD
}


def map_surveys_to_collection_exercises(surveys, collection_exercises) -> list:
    survey_data = {
        survey['id']: {
            'surveyId': survey['id'],
            'collectionInstrumentType': 'eq',
            'shortName': survey['shortName'],
            'longName': survey['longName'],
            'surveyRef': survey['surveyRef'],
            'collectionExercises': []
        } for survey in surveys
    }

    for survey in survey_data.values():
        if survey['surveyId'] in SEFT_SURVEYS:
            survey['collectionInstrumentType'] = 'seft'

    for collection_exercise in collection_exercises:
        try:
            survey_data[collection_exercise['surveyId']]['collectionExercises'].append(
                {
                    'collectionExerciseId': collection_exercise['id'],
                    'userDescription': collection_exercise['userDescription'],
                    'exerciseRef': collection_exercise['exerciseRef']
                }
            )
        except KeyError as e:
            if str(e) == f"'{collection_exercise['surveyId']}'":
                message = 'Reference to unknown survey id in collection exercise'
                logger.error(message, collection_exercise_id=collection_exercise['id'])
                raise UnknownSurveyError(
                    message=message,
                    survey_id=['surveyId'])
            else:
                raise

    return list(survey_data.values())


def map_collection_exercise_id_to_survey_id(surveys_to_collection_exercises) -> dict:
    collection_exercises_to_survey_ids = {}
    for survey in surveys_to_collection_exercises:
        for collection_exercise in survey['collectionExercises']:
            collection_exercises_to_survey_ids[collection_exercise['collectionExerciseId']] = {
                'surveyId': survey['surveyId'],
                'collectionInstrumentType': survey['collectionInstrumentType'],
                'shortName': survey['shortName'],
                'longName': survey['longName'],
                'userDescription': collection_exercise['userDescription'],
                'exerciseRef': collection_exercise['exerciseRef']
            }

    return collection_exercises_to_survey_ids


def fetch_survey_and_collection_exercise_metadata() -> (list, dict):
    collection_exercises = get_collection_exercise_list()
    live_collection_exercises = _filter_ready_collection_exercises(collection_exercises)
    surveys = get_survey_list()

    surveys_to_collection_exercises = map_surveys_to_collection_exercises(surveys, live_collection_exercises)
    collection_exercises_to_survey_ids = map_collection_exercise_id_to_survey_id(surveys_to_collection_exercises)

    return surveys_to_collection_exercises, collection_exercises_to_survey_ids


def _filter_ready_collection_exercises(collection_exercises: list) -> list:
    return [
        collection_exercise
        for collection_exercise in collection_exercises
        if collection_exercise['state'] in {'READY_FOR_LIVE', 'LIVE'}
    ]
