from flask import current_app
import requests
from requests.auth import HTTPBasicAuth
import requests.exceptions
from structlog import get_logger

from app.exceptions import ApiConnectionError

logger = get_logger()


def get_collection_exercise_list():
    url = f'{current_app.config["COLLECTION_EXERCISE_URL"]}collectionexercises'
    logger.debug('Attempting to retrieve collection exercises')
    try:
        response = requests.get(
            url,
            auth=HTTPBasicAuth(current_app.config['AUTH_USERNAME'],
                               current_app.config['AUTH_PASSWORD']))
    except requests.exceptions.ConnectionError:
        raise ApiConnectionError('Failed to connect to collection exercise service')
    if response.status_code != 200:
        logger.error('Failed to retrieve collection exercises',
                     status_code=response.status_code,
                     response=response.content)
        response.raise_for_status()
    logger.debug('Successfully retrieved collection exercises')
    return response.json()
