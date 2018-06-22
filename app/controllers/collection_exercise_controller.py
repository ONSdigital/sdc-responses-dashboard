from flask import current_app, abort
import requests
from requests.auth import HTTPBasicAuth


def get_collection_exercise_list():
    url = f'{current_app.config["COLLECTION_EXERCISE_URL"]}collectionexercises'
    response = requests.get(
        url,
        auth=HTTPBasicAuth(current_app.config['AUTH_USERNAME'],
                           current_app.config['AUTH_PASSWORD']))
    if response.status_code != 200:
        abort(500)
    return response.json()
