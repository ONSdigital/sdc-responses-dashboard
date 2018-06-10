import requests

from flask import current_app, abort
from requests.auth import HTTPBasicAuth


def get_collection_exercise_list():
    current_app.logger.debug('Retrieving collection exercises list')
    url = f'{current_app.config["COLLECTION_EXERCISE_URL"]}/collectionexercises'
    response = requests.get(
        url,
        auth=HTTPBasicAuth(current_app.config['AUTH_USERNAME'],
                           current_app.config['AUTH_PASSWORD']))
    if response.status_code != 200:
        current_app.logger.error('Failed to retrieve collection exercises list')
        abort(500)
    current_app.logger.debug('Successfully retrieved collection exercises list')
    return response.json()
