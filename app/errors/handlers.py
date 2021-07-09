from flask import render_template
from structlog import get_logger

ERROR_MESSAGE_NOT_FOUND = "Sorry, we could not find the page you were looking for."
ERROR_MESSAGE_UNEXPECTED = "Sorry, something has gone wrong."

logger = get_logger()


def not_found_error(error):
    logger.debug("Handling 404 error", error=error)
    return (
        render_template(
            "errors/error.html", status_code=404, error_name="Not found error", error_msg=ERROR_MESSAGE_NOT_FOUND
        ),
        404,
    )


def internal_server_error(error):
    logger.error("Handling 500 error", error=error)

    return (
        render_template(
            "errors/error.html", status_code=500, error_name="Internal server error", error_msg=ERROR_MESSAGE_UNEXPECTED
        ),
        500,
    )


def api_connection_error(error):
    logger.error(error.message)

    return (
        render_template(
            "errors/error.html", status_code=500, error_name="Internal server error", error_msg=ERROR_MESSAGE_UNEXPECTED
        ),
        500,
    )
