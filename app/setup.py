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

    _configure_logger(app.config['LOGGING_LEVEL'])

    add_blueprints(app)

    return app


def add_blueprints(app):

    from app.api.health import health_blueprint
    from app.api.surveys import surveys_blueprint
    from app.api.survey import survey_blueprint

    app.register_blueprint(health_blueprint)
    app.register_blueprint(surveys_blueprint)
    app.register_blueprint(survey_blueprint)


def _configure_logger(level):
    logging.basicConfig(stream=sys.stdout, level=level)

    structlog.configure(
        processors=[
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M.%S"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            JSONRenderer(indent=True)
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
