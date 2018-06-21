from flask import current_app, abort
import requests
from requests.exceptions import ConnectionError
from requests.auth import HTTPBasicAuth
from structlog import get_logger

logger = get_logger()


def get_collection_exercise_list():
    url = f'{current_app.config["COLLECTION_EXERCISE_URL"]}collectionexercises'
    try:
        logger.debug("Attempting to retrieve collection exercises")
        response = requests.get(
            url,
            auth=HTTPBasicAuth(current_app.config['AUTH_USERNAME'],
                               current_app.config['AUTH_PASSWORD']))
    except ConnectionError as e:
        logger.error("Failed to connect to collection exercise service", error=e)
        abort(500)
    if response.status_code != 200:
        logger.error("Failed to retrieve collection exercise")
        response.raise_for_status()
    logger.debug("Successfully retrieved collection exercises")
    return response.json()
