from flask import current_app
import requests
from structlog import get_logger

from app.exceptions import APIConnectionError

logger = get_logger()


def get_reporting_details(collection_instrument_type, collex_id):
    logger.debug('Fetching report for collection exercise',
                 collex_id=collex_id,
                 collection_instrument_type=collection_instrument_type)
    url = f'{current_app.config["REPORTING_URL"]}/reporting-api/v1/response-dashboard' \
          f'/{collection_instrument_type}/collection-exercise/{collex_id}'
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        raise APIConnectionError('Failed to connect to reporting service')

    response.raise_for_status()

    logger.debug('Successfully fetched report for collection exercise',
                 collex_id=collex_id,
                 collection_instrument_type=collection_instrument_type)
    return response.text
