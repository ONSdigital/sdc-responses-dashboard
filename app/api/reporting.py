import json

from flask import Blueprint, abort
from requests import HTTPError
from structlog import get_logger

from app.controllers.reporting_controller import get_reporting_details
from app.validators import parse_uuid

reporting_blueprint = Blueprint(name='reporting', import_name=__name__, url_prefix='/dashboard')

logger = get_logger()


@reporting_blueprint.route('/reporting/<collection_instrument_type>'
                           '/survey/<survey_id>'
                           '/collection-exercise/<collex_id>', methods=['GET'])
def reporting_details(collection_instrument_type, survey_id, collex_id):
    ci_types = {'eq', 'seft'}

    parsed_survey_id = parse_uuid(survey_id)
    if not parsed_survey_id:
        logger.debug('Malformed collection exercise ID', invalid_survey_id=survey_id)
        abort(404, 'Malformed collection exercise ID')

    parsed_collex_id = parse_uuid(collex_id)
    if not parsed_collex_id:
        logger.debug('Malformed collection exercise ID', invalid_collex_id=collex_id)
        abort(404, 'Malformed collection exercise ID')

    if not collection_instrument_type.lower() in ci_types:
        logger.debug('Invalid CI type', ci_type=collection_instrument_type)
        abort(404, 'Invalid CI type')

    try:
        report = get_reporting_details(parsed_survey_id, parsed_collex_id)
    except HTTPError:
        logger.debug('Invalid collection exercise or survey id')
        abort(404)

    if collection_instrument_type == 'seft':
        report['report']['uploads'] = report['report'].pop('completed')
        report['report']['downloads'] = report['report'].pop('inProgress') + report['report']['uploads']

    return json.dumps(report)
