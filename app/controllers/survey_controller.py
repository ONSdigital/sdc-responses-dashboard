from flask import current_app as app, abort
import requests
import requests.exceptions
from requests.auth import HTTPBasicAuth
from structlog import get_logger

logger = get_logger()


def get_survey_list():
    url = f'{app.config["SURVEY_URL"]}surveys'
    logger.debug('Attempting to retrieve surveys')
    try:
        response = requests.get(
            url,
            auth=HTTPBasicAuth(app.config['AUTH_USERNAME'],
                               app.config['AUTH_PASSWORD']))
    except requests.exceptions.ConnectionError:
        logger.error('Failed to connect to survey service')
        abort(500)
    if response.status_code != 200:
        logger.error('Failed to retrieve surveys',
                     status_code=response.status_code,
                     response=response.content)
        response.raise_for_status()
    logger.debug('Successfully retrieved surveys')
    return response.json()
