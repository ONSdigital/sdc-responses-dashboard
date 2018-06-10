import requests

from flask import current_app, abort
from requests.auth import HTTPBasicAuth


def get_survey_list():
    current_app.logger.debug('Retrieving surveys list')
    url = f'{current_app.config["SURVEY_URL"]}/surveys'
    response = requests.get(
        url,
        auth=HTTPBasicAuth(current_app.config['AUTH_USERNAME'],
                           current_app.config['AUTH_PASSWORD']))
    if response.status_code != 200:
        current_app.logger.error('Failed to retrieve survey list')
        abort(500)
    current_app.logger.debug('Successfully retrieved surveys list')
    return response.json()
