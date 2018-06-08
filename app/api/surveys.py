from datetime import datetime
import json
import uuid

from flask import Blueprint, Response

surveys_blueprint = Blueprint(name='surveys', import_name=__name__)


# Hardcoded example response for development
@surveys_blueprint.route('/surveys', methods=['GET'])
def get_report():
    return Response(
        json.dumps({
            'timestamp': datetime.now().timestamp(),
            'surveys': [
                {
                    'shortName': 'BRES',
                    'surveyId': 'cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87',
                    'collectionExercises': [
                        {
                            'period': 2018,
                            'collexId': '8d50b535-e852-433c-af1f-e7d027533078'
                        },
                        {
                            'period': 2017,
                            'collexId': str(uuid.uuid4())
                        },
                        {
                            'period': 2016,
                            'collexId': str(uuid.uuid4())
                        }
                    ]
                },
                {
                    'shortName': 'BRAS',
                    'surveyId': str(uuid.uuid4()),
                    'collectionExercises': [
                        {
                            'period': 2018,
                            'collexId': str(uuid.uuid4())
                        }
                    ]
                },
                {
                    'shortName': 'BRIS',
                    'surveyId': str(uuid.uuid4()),
                    'collectionExercises': [
                        {
                            'period': 2018,
                            'collexId': str(uuid.uuid4())
                        }
                    ]
                },
                {
                    'shortName': 'BRUS',
                    'surveyId': str(uuid.uuid4()),
                    'collectionExercises': [
                        {
                            'period': 2018,
                            'collexId': str(uuid.uuid4())
                        }
                    ]
                },
                {
                    'shortName': 'BROS',
                    'surveyId': str(uuid.uuid4()),
                    'collectionExercises': [
                        {
                            'period': 2018,
                            'collexId': str(uuid.uuid4())
                        }
                    ]
                }
            ]
        }),
        content_type='application/json')
