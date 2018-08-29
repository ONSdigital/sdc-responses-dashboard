from flask import Blueprint, render_template, current_app, abort

from app.common.survey_metadata import fetch_survey_and_collection_exercise_metadata

dashboard_blueprint = Blueprint(name='dashboard', import_name=__name__)


@dashboard_blueprint.before_request
def clear_trailing():
    from flask import redirect, request

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
def get_survey_details(collection_exercise_id):
    surveys_metadata, collection_exercise_metadata = fetch_survey_and_collection_exercise_metadata()
    try:
        collection_exercise = collection_exercise_metadata[collection_exercise_id]
    except KeyError:
        abort(404)

    return render_template(
        'reporting.html',
        collex_id=collection_exercise_id,
        all_surveys=surveys_metadata,
        collection_instrument_type=collection_exercise['collectionInstrumentType'],
        survey_short_name=collection_exercise['shortName'],
        survey_long_name=collection_exercise['longName'],
        collection_exercise=collection_exercise['userDescription'],
        reporting_refresh_cycle=int(current_app.config['REPORTING_REFRESH_CYCLE'])
    )


@dashboard_blueprint.after_request
def add_cache_control(response):
    response.cache_control.no_cache = True
    return response
