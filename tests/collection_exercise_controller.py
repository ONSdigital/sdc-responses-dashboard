import requests
from requests.auth import HTTPBasicAuth

from app.exceptions import APIConnectionError
from tests.test_config import TestConfig


def get_collection_exercise_list():
    url = f'{TestConfig.COLLECTION_EXERCISE_URL}collectionexercises'
    try:
        response = requests.get(
            url,
            auth=HTTPBasicAuth(TestConfig.AUTH_USERNAME,
                               TestConfig.AUTH_PASSWORD))
    except requests.exceptions.ConnectionError:
        raise APIConnectionError('Failed to connect to collection exercise service')
    if response.status_code != 200:
        response.raise_for_status()
    return response.json()
