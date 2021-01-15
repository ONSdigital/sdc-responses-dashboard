from flask import Blueprint, abort, current_app, render_template, redirect, request

from app.survey_metadata import fetch_survey_and_collection_exercise_metadata

dashboard_blueprint = Blueprint(name='dashboard', import_name=__name__, url_prefix='/dashboard')


@dashboard_blueprint.before_request
def clear_trailing():
    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])


@dashboard_blueprint.route('/', methods=['GET'])
def get_surveys():
    surveys_metadata, _ = fetch_survey_and_collection_exercise_metadata()

    return render_template(
        'dashboard.html',
        all_surveys=surveys_metadata
    )


@dashboard_blueprint.route('/collection-exercise/<collection_exercise_id>', methods=['GET'])
def get_dashboard_for_collection_exercise(collection_exercise_id):
    surveys_metadata, collection_exercise_metadata = fetch_survey_and_collection_exercise_metadata()
    try:
        collection_exercise = collection_exercise_metadata[collection_exercise_id]
        return render_template(
            'reporting.html',
            collex_id=collection_exercise_id,
            all_surveys=surveys_metadata,
            survey_short_name=collection_exercise['shortName'],
            survey_long_name=collection_exercise['longName'],
            survey_id=collection_exercise['surveyId'],
            collection_exercise_description=collection_exercise['userDescription'],
            reporting_refresh_cycle=int(current_app.config['REPORTING_REFRESH_CYCLE_IN_SECONDS'])
        )
    except KeyError:
        abort(404)


@dashboard_blueprint.after_request
def add_cache_control(response):
    response.cache_control.no_cache = True
    return response
