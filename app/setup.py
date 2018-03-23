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

    from app.api.routes import routes_blueprint
    app.register_blueprint(routes_blueprint)
