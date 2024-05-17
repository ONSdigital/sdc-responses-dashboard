import logging
import os
import sys

import structlog
from flask import Flask, current_app, url_for
from flask_cors import CORS
from structlog import wrap_logger

import config
from app.api.health import health_blueprint
from app.api.reporting import reporting_blueprint
from app.errors.handlers import (
    api_connection_error,
    internal_server_error,
    not_found_error,
)
from app.exceptions import APIConnectionError, MissingConfigError
from app.views.dashboard import dashboard_blueprint


def create_app():
    app_config = getattr(config, os.getenv("APP_SETTINGS", "Config"))
    check_required_config(app_config)

    app = Flask(__name__, static_url_path="/dashboard/static")
    app.url_map.strict_slashes = False

    CORS(app)

    app.config.from_object(app_config)

    _configure_logger(app.config["LOGGING_LEVEL"])
    logger = wrap_logger(logging.getLogger(__name__))
    logger.info("Logger created", log_level=app.config["LOGGING_LEVEL"])
    logger.debug("App configuration set", config=app_config)

    add_blueprints(app)
    add_error_handlers(app)

    @app.context_processor
    def override_url_for():
        return dict(url_for=versioned_url_for)

    return app


def add_blueprints(app):
    app.register_blueprint(health_blueprint)
    app.register_blueprint(dashboard_blueprint)
    app.register_blueprint(reporting_blueprint)


def add_error_handlers(app):
    app.register_error_handler(404, not_found_error)
    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(APIConnectionError, api_connection_error)


def versioned_url_for(endpoint, **values):
    if endpoint == "static":
        filename = values.get("filename", None)
        if filename:
            values["filename"] = filename
            values["q"] = current_app.config["STATIC_ASSETS_VERSION"]

    return url_for(endpoint, **values)


def _configure_logger(log_level: str = "INFO") -> None:
    def add_service(_, __, event_dict: dict) -> dict:
        """
        Add the service name to the event dict.
        """
        event_dict["service"] = os.getenv("NAME", "sdc-responses-dashboard")
        return event_dict

    def add_severity_level(_, method_name: str, event_dict: dict) -> dict:
        """
        Adds the log level to the event dict.
        """
        event_dict["severity"] = method_name
        return event_dict

    def parse_exception(_, __, event_dict: dict) -> dict:
        """
        Formats the exception string in the event_dict.
        """
        exception = event_dict.get("exception")
        if exception:
            event_dict["exception"] = exception.replace('"', "'").split("\n")
        return event_dict

    logging.basicConfig(format="%(message)s", stream=sys.stdout, level=log_level)

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            add_severity_level,
            add_service,
            parse_exception,
            structlog.processors.format_exc_info,
            structlog.processors.TimeStamper(fmt="%Y-%m-%dT%H:%M%s", utc=True, key="created_at"),
            structlog.processors.JSONRenderer(indent=None),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(logging.getLevelName(log_level)),
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )


def check_required_config(app_config):
    missing_vars = {var for var in config.REQUIRED_ENVIRONMENT_VARIABLES if not vars(app_config).get(var)}
    if missing_vars:
        raise MissingConfigError(missing_vars)
