import requests
from flask import current_app
from structlog import get_logger

from app.exceptions import APIConnectionError

logger = get_logger()


def get_reporting_details(survey_id, collex_id):
    logger.info("Fetching report for collection exercise", collex_id=collex_id, survey_id=survey_id)
    url = (
        f'{current_app.config["REPORTING_URL"]}/reporting-api/v1/response-dashboard'
        f"/survey/{survey_id}/collection-exercise/{collex_id}"
    )
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        raise APIConnectionError("Failed to connect to reporting service")

    response.raise_for_status()

    logger.info("Successfully fetched report for collection exercise", collex_id=collex_id, survey_id=survey_id)
    return response.json()
