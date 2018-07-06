from structlog import get_logger
from flask import render_template

logger = get_logger()


def not_found_error(error):
    custom_error_msg = 'Sorry, we could not find the page you were looking for.'

    logger.error(error.name,
                 error=error,
                 status_code=error.code,
                 description=error.description)

    return render_template('errors/error.html',
                           status_code=error.code,
                           error_name=error.name,
                           error_msg=custom_error_msg), 404


def internal_server_error(error):
    custom_error_msg = 'Sorry, something has gone wrong.'

    logger.error(error.name,
                 error=error,
                 status_code=error.code,
                 description=error.description)

    return render_template('errors/error.html',
                           status_code=error.code,
                           error_name=error.name,
                           error_msg=custom_error_msg), 500
