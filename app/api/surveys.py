from datetime import datetime
import json
import uuid

from flask import Blueprint, Response

from app.controllers.collection_exercise_controller import get_collection_exercise_list
from app.controllers.survey_controller import get_survey_list

surveys_blueprint = Blueprint(name='surveys', import_name=__name__)


# Hardcoded example response for development
@surveys_blueprint.route('/surveys', methods=['GET'])
def get_surveys():
    surveys = get_survey_list()
    collexs = get_collection_exercise_list()
    survey_data = _process_survey_metadata(surveys, collexs)
    return Response(
        json.dumps({
            'timestamp': datetime.now().timestamp(),
            'surveys': survey_data
        }),
        content_type='application/json')


# TODO remove once no longer required
# Example response endpoint for convenience in development
@surveys_blueprint.route('/surveys/example', methods=['GET'])
def get_surveys_example():
    return Response(
        json.dumps({
            'timestamp': datetime.now().timestamp(),
            'surveys': [
                {
                    'shortName': 'BRES',
                    'surveyId': 'cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87',
                    'surveyRef': '221',
                    'collectionExercises': [
                        {
                            'exerciseRef': 2018,
                            'collexId': '8d50b535-e852-433c-af1f-e7d027533078'
                        },
                        {
                            'exerciseRef': 2017,
                            'collexId': str(uuid.uuid4())
                        },
                        {
                            'exerciseRef': 2016,
                            'collexId': str(uuid.uuid4())
                        }
                    ]
                },
                {
                    'shortName': 'BRAS',
                    'surveyId': str(uuid.uuid4()),
                    'surveyRef': '222',
                    'collectionExercises': [
                        {
                            'exerciseRef': 2018,
                            'collexId': str(uuid.uuid4())
                        }
                    ]
                },
                {
                    'shortName': 'BRIS',
                    'surveyId': str(uuid.uuid4()),
                    'surveyRef': '223',
                    'collectionExercises': [
                        {
                            'exerciseRef': 2018,
                            'collexId': str(uuid.uuid4())
                        }
                    ]
                },
                {
                    'shortName': 'BRUS',
                    'surveyId': str(uuid.uuid4()),
                    'surveyRef': '224',
                    'collectionExercises': [
                        {
                            'exerciseRef': 2018,
                            'collexId': str(uuid.uuid4())
                        }
                    ]
                },
                {
                    'shortName': 'BROS',
                    'surveyId': str(uuid.uuid4()),
                    'surveyRef': '225',
                    'collectionExercises': [
                        {
                            'exerciseRef': 2018,
                            'collexId': str(uuid.uuid4())
                        }
                    ]
                }
            ]
        }),
        content_type='application/json')


def _process_survey_metadata(surveys, collection_exercises):
    survey_data = {
        survey['id']: {
            'surveyId': survey['id'],
            'shortName': survey['shortName'],
            'surveyRef': survey['surveyRef'],
            'collectionExercises': []
        }
        for survey in surveys
    }

    for collection_exercise in collection_exercises:
        survey_data[collection_exercise['surveyId']]['collectionExercises'].append(
            {
                'collexId': collection_exercise['id'],
                'exerciseRef': collection_exercise['exerciseRef']
            }
        )

    return list(survey_data.values())

