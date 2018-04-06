import os

from flask import Flask

import config


def create_app():
    app = Flask(__name__)
    app_config = getattr(config, os.getenv('APP_SETTINGS', 'Config'))
    app.config.from_object(app_config)
    add_blueprints(app)

    return app


def add_blueprints(app):

    from app.api.health import health_blueprint
    from app.api.report import report_blueprint

    app.register_blueprint(health_blueprint)
    app.register_blueprint(report_blueprint)
