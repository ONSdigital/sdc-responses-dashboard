from structlog import get_logger
from flask import render_template

logger = get_logger()


def not_found_error(error):
    custom_error_msg = 'Sorry, we could not find the page you were looking for.'

    logger.error("Handling 404 error",
                 error=error)

    return render_template('errors/error.html',
                           status_code=404,
                           error_name='Not found error',
                           error_msg=custom_error_msg), 404


def internal_server_error(error):
    custom_error_msg = 'Sorry, something has gone wrong.'

    logger.error("Handling 500 error",
                 error=error)

    return render_template('errors/error.html',
                           status_code=500,
                           error_name='Internal server error',
                           error_msg=custom_error_msg), 500
