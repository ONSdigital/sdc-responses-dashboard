import logging
import os
import sys

from flask import Flask
from flask_cors import CORS
import structlog
from structlog.processors import JSONRenderer

import config


def create_app():

    app = Flask(__name__)

    CORS(app)

    app_config = getattr(config, os.getenv('APP_SETTINGS', 'Config'))
    app.config.from_object(app_config)

    _configure_logger(level=app.config['LOGGING_LEVEL'],
                      indent=app.config['LOGGING_JSON_INDENT'])

    add_blueprints(app)
    add_error_handlers(app)

    return app


def add_blueprints(app):

    from app.api.health import health_blueprint
    from app.views.dashboard import dashboard_blueprint

    app.register_blueprint(health_blueprint)
    app.register_blueprint(dashboard_blueprint)


def add_error_handlers(app):

    from app.errors.handlers import not_found_error, internal_server_error

    app.register_error_handler(404, not_found_error)
    app.register_error_handler(500, internal_server_error)


def _configure_logger(level='INFO', indent=False):
    logging.basicConfig(stream=sys.stdout, level=level, format='%(asctime)s %(levelname)s %(message)s')

    structlog.configure(
        processors=[
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt='%Y-%m-%d %H:%M.%S', utc=True),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            JSONRenderer(indent=indent)
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
