from flask import Blueprint, jsonify

routes_blueprint = Blueprint(name='routes', import_name=__name__)


@routes_blueprint.route('/')
def index():
    return jsonify({'Hello My': 'FRIENDS!'})
