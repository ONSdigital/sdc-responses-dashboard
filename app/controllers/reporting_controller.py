import requests
from flask import current_app, abort


def get_reporting_details(collectioninstrumenttype, collex_id):

    url = f'{current_app.config["REPORTING_URL"]}reporting-api/v1/response-dashboard' \
          f'/{collectioninstrumenttype}/collection-exercise/{collex_id}'
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        abort(500)

    response.raise_for_status()

    return response.text
