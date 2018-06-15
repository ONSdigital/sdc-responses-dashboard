import uuid
from datetime import datetime


from flask import Blueprint, render_template, json
from app.api.nocache import nocache
survey_blueprint = Blueprint(name='survey', import_name=__name__)

all_surveys = {
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
                        },
{
                            'exerciseRef': 2015,
                            'collexId': str(uuid.uuid4())
                        },
{
                            'exerciseRef': 2014,
                            'collexId': str(uuid.uuid4())
                        },
{
                            'exerciseRef': 2013,
                            'collexId': str(uuid.uuid4())
                        },
{
                            'exerciseRef': 2012,
                            'collexId': str(uuid.uuid4())
                        },
{
                            'exerciseRef': 2011,
                            'collexId': str(uuid.uuid4())
                        },
{
                            'exerciseRef': 2010,
                            'collexId': str(uuid.uuid4())
                        },
{
                            'exerciseRef': 2009,
                            'collexId': str(uuid.uuid4())
                        },
{
                            'exerciseRef': 2008,
                            'collexId': str(uuid.uuid4())
                        },
{
                            'exerciseRef': 2007,
                            'collexId': str(uuid.uuid4())
                        },
{
                            'exerciseRef': 2006,
                            'collexId': str(uuid.uuid4())
                        },
{
                            'exerciseRef': 2005,
                            'collexId': str(uuid.uuid4())
                        },
{
                            'exerciseRef': 2004,
                            'collexId': str(uuid.uuid4())
                        },
{
                            'exerciseRef': 2003,
                            'collexId': str(uuid.uuid4())
                        },
{
                            'exerciseRef': 2002,
                            'collexId': str(uuid.uuid4())
                        },
{
                            'exerciseRef': 2001,
                            'collexId': str(uuid.uuid4())
                        },
{
                            'exerciseRef': 2000,
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
        }


@survey_blueprint.route('/survey/collection-exercise/<collection_exercise_id>', methods=['GET'])
@nocache
def get_survey(collection_exercise_id):
    return render_template('survey.html', collex_id=collection_exercise_id, all_surveys=all_surveys)