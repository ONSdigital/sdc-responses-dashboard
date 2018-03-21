from flask import Flask, logging


def create_app():

    app = Flask(__name__)
    add_blueprints(app)

    return app


def add_blueprints(app):

    from app.api.routes import routes_blueprint
    app.register_blueprint(routes_blueprint)
