from flask import Blueprint, abort
from requests import HTTPError
from structlog import get_logger

from app.controllers.reporting_controller import get_reporting_details
from app.common.validators import parse_uuid

reporting_blueprint = Blueprint(name='reporting', import_name=__name__)

logger = get_logger()


@reporting_blueprint.route('/reporting/<collection_instrument_type>/collection-exercise/<collex_id>', methods=['GET'])
def reporting_details(collection_instrument_type, collex_id):

    ci_types = {'eq', 'seft'}

    collex_id = parse_uuid(collex_id)

    if not collex_id:
        logger.debug('Malformed collection exercise ID', invalid_id=collex_id)
        abort(404, 'Malformed collection exercise ID')

    if not collection_instrument_type.lower() in ci_types:
        logger.debug('Invalid CI type', ci_type=collection_instrument_type)
        abort(404, 'Invalid CI type')

    try:
        report = get_reporting_details(collection_instrument_type, collex_id)
    except HTTPError:
        logger.debug('Invalid Collection exercise id')
        abort(404)

    return report
