from flask import current_app as app, abort
import requests
from requests.auth import HTTPBasicAuth


def get_survey_list():
    url = f'{app.config["SURVEY_URL"]}surveys'
    response = requests.get(
        url,
        auth=HTTPBasicAuth(app.config['AUTH_USERNAME'],
                           app.config['AUTH_PASSWORD']))
    if response.status_code != 200:
        abort(500)
    return response.json()
