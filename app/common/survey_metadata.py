from app.controllers.collection_exercise_controller import get_collection_exercise_list
from app.controllers.survey_controller import get_survey_list
from app.exceptions import UnknownSurveyError


def map_surveys_to_collection_exercises(surveys, collection_exercises) -> list:
    survey_data = {
        survey['id']: {
            'surveyId': survey['id'],
            'shortName': survey['shortName'],
            'surveyRef': survey['surveyRef'],
            'collectionExercises': []
        } for survey in surveys
    }

    for collection_exercise in collection_exercises:
        try:
            survey_data[collection_exercise['surveyId']]['collectionExercises'].append(
                {
                    'collexId': collection_exercise['id'],
                    'collexName': collection_exercise['name']
                }
            )
        except KeyError as e:
            if str(e) == f"'{collection_exercise['surveyId']}'":
                raise UnknownSurveyError(
                    message='Reference to unknown survey id in collection exercise',
                    survey_id=['surveyId'])
            else:
                raise

    return list(survey_data.values())


def map_collection_exercise_id_to_survey_id(surveys_to_collection_exercises) -> dict:
    collection_exercises_to_survey_ids = {}
    for survey in surveys_to_collection_exercises:
        for collection_exercise in survey['collectionExercises']:
            collection_exercises_to_survey_ids[collection_exercise['collexId']] = {
                'surveyId': survey['surveyId'],
                'shortName': survey['shortName'],
                'collexName': collection_exercise['collexName']
            }

    return collection_exercises_to_survey_ids


def fetch_survey_and_collection_exercise_metadata() -> (list, dict):
    collection_exercises = get_collection_exercise_list()
    surveys = get_survey_list()

    surveys_to_collection_exercises = map_surveys_to_collection_exercises(surveys, collection_exercises)
    collection_exercises_to_survey_ids = map_collection_exercise_id_to_survey_id(surveys_to_collection_exercises)

    return surveys_to_collection_exercises, collection_exercises_to_survey_ids
