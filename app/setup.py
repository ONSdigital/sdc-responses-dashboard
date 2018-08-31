import logging
import os
import sys

from flask import Flask
from flask_cors import CORS
import structlog
from structlog.processors import JSONRenderer
from structlog.threadlocal import wrap_dict

from app.exceptions import MissingConfigError
import config


def create_app():

    app_config = getattr(config, os.getenv('APP_SETTINGS', 'Config'))
    check_required_config(app_config)

    app = Flask(__name__)
    app.url_map.strict_slashes = False

    CORS(app)

    app.config.from_object(app_config)

    _configure_logger(level=app.config['LOGGING_LEVEL'],
                      indent=int(app.config['LOGGING_JSON_INDENT']))

    add_blueprints(app)
    add_error_handlers(app)

    return app


def add_blueprints(app):

    from app.api.health import health_blueprint
    from app.views.dashboard import dashboard_blueprint
    from app.api.reporting import reporting_blueprint

    app.register_blueprint(health_blueprint)
    app.register_blueprint(dashboard_blueprint)
    app.register_blueprint(reporting_blueprint)


def add_error_handlers(app):

    from app.errors.handlers import not_found_error, internal_server_error

    app.register_error_handler(404, not_found_error)
    app.register_error_handler(500, internal_server_error)


def _configure_logger(level='INFO', indent=0):
    logging.basicConfig(stream=sys.stdout, level=level, format='%(message)s')

    def parse_exception(_, __, event_dict):
        exception = event_dict.get('exception')
        if exception:
            event_dict['exception'] = exception.replace("\"", "'").split("\n")
        return event_dict

    def add_service(logger, method_name, event_dict):  # pylint: disable=unused-argument
        """
        Add the service name to the event dict.
        """
        event_dict['service'] = os.getenv('NAME', 'sdc-responses-dashboard')
        return event_dict

    structlog.configure(
        processors=[
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.filter_by_level,
            add_service,
            structlog.processors.TimeStamper(fmt='%Y-%m-%dT%H:%M%s', utc=True),
            structlog.processors.format_exc_info,
            parse_exception,
            JSONRenderer(indent=indent)
        ],
        context_class=wrap_dict(dict),
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )



def check_required_config(app_config):
    missing_vars = {var for var in config.REQUIRED_ENVIRONMENT_VARIABLES if not vars(app_config).get(var)}
    if missing_vars:
        raise MissingConfigError(missing_vars)
