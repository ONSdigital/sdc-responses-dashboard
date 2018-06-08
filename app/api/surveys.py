from datetime import datetime
import json
import uuid

from flask import Blueprint, Response

report_blueprint = Blueprint(name='surveys', import_name=__name__)


# Hardcoded example response for development
@report_blueprint.route('/surveys', methods=['GET'])
def get_report():
    return Response(
        json.dumps({
            'timestamp': datetime.now().timestamp()
            [
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
                            'collexId': uuid.uuid4()
                        },
                        {
                            'period': 2016,
                            'collexId': uuid.uuid4()
                        }
                    ]
                },
                {
                    'shortName': 'BRAS',
                    'surveyId': uuid.uuid4(),
                    'collectionExercises': [
                        {
                            'period': 2018,
                            'collexId': uuid.uuid4()
                        }
                    ]
                },
                {
                    'shortName': 'BRIS',
                    'surveyId': uuid.uuid4(),
                    'collectionExercises': [
                        {
                            'period': 2018,
                            'collexId': uuid.uuid4()
                        }
                    ]
                },
                {
                    'shortName': 'BRUS',
                    'surveyId': uuid.uuid4(),
                    'collectionExercises': [
                        {
                            'period': 2018,
                            'collexId': uuid.uuid4()
                        }
                    ]
                },
                {
                    'shortName': 'BROS',
                    'surveyId': uuid.uuid4(),
                    'collectionExercises': [
                        {
                            'period': 2018,
                            'collexId': uuid.uuid4()
                        }
                    ]
                }
            ]
        }),
        content_type='application/json')
