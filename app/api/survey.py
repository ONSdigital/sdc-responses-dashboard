from pprint import pprint

from flask import Blueprint, render_template, current_app, abort

from app.api.nocache import nocache
from app.common.survey_metadata import fetch_survey_and_collection_exercise_metadata

survey_blueprint = Blueprint(name='survey', import_name=__name__)


@survey_blueprint.route('/survey/collection-exercise/<collection_exercise_id>', methods=['GET'])
@nocache
def get_survey(collection_exercise_id):

    surveys_metadata, collection_exercise_metadata = fetch_survey_and_collection_exercise_metadata()

    try:
        collection_exercise_name = collection_exercise_metadata[collection_exercise_id]['collexName']
    except KeyError:
        abort(404)

    pprint(surveys_metadata)
    print(collection_exercise_id)
    print(collection_exercise_name)

    return render_template(
        'survey.html',
        collex_id=collection_exercise_id,
        all_surveys=surveys_metadata,
        collection_exercise_name=collection_exercise_name,
        reporting_url=current_app.config['REPORTING_URL']
    )
