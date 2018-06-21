from flask import current_app as app, abort
import requests
from requests.auth import HTTPBasicAuth
from structlog import get_logger

logger = get_logger()


def get_survey_list():
    url = f'{app.config["SURVEY_URL"]}surveys'
    try:
        logger.debug("Attempting to retrieve surveys")
        response = requests.get(
            url,
            auth=HTTPBasicAuth(app.config['AUTH_USERNAME'],
                               app.config['AUTH_PASSWORD']))
    except ConnectionError as e:
        logger.error("Failed to connect to survey service")
        abort(500)
    if response.status_code != 200:
        logger.error("Failed to retrieve surveys")
        response.raise_for_status()
    logger.debug("Successfully retrieved surveys")
    return response.json()
