from flask import Blueprint, render_template, current_app, abort

from app.api.nocache import nocache
from app.common.survey_metadata import fetch_survey_and_collection_exercise_metadata

dashboard_blueprint = Blueprint(name='dashboard', import_name=__name__)


@dashboard_blueprint.route('/dashboard/collection-exercise/<collection_exercise_id>', methods=['GET'])
@nocache
def get_survey(collection_exercise_id):
    surveys_metadata, collection_exercise_metadata = fetch_survey_and_collection_exercise_metadata()

    try:
        collection_exercise = collection_exercise_metadata[collection_exercise_id]
    except KeyError:
        abort(404)

    collection_exercise_name = f"{collection_exercise['shortName']} - {collection_exercise['userDescription']}"

    return render_template(
        'dashboard.html',
        collex_id=collection_exercise_id,
        all_surveys=surveys_metadata,
        collection_exercise_name=collection_exercise_name,
        reporting_url=current_app.config['REPORTING_URL']
    )
