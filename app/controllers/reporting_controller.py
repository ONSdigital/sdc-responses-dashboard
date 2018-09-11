from flask import current_app
import requests
from requests.auth import HTTPBasicAuth
from structlog import get_logger

from app.exceptions import APIConnectionError

logger = get_logger()


def get_reporting_details(collectioninstrumenttype, collex_id):
    logger.debug('Fetching report for collection exercise',
                 collex_id=collex_id,
                 collection_instrument_type=collectioninstrumenttype)
    url = f'{current_app.config["REPORTING_URL"]}reporting-api/v1/response-dashboard' \
          f'/{collectioninstrumenttype}/collection-exercise/{collex_id}'
    try:
        response = requests.get(url,
                                auth=HTTPBasicAuth(current_app.config['AUTH_USERNAME'],
                                                   current_app.config['AUTH_PASSWORD']))
    except requests.exceptions.ConnectionError:
        raise APIConnectionError('Failed to connect to reporting service')

    response.raise_for_status()

    logger.debug('Successfully fetched report for collection exercise',
                 collex_id=collex_id,
                 collection_instrument_type=collectioninstrumenttype)
    return response.text
