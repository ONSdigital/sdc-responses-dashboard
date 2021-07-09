from flask import Blueprint, jsonify

health_blueprint = Blueprint(name="health", import_name=__name__, url_prefix="/dashboard")


@health_blueprint.route("/health")
def health():
    return jsonify({"status": "healthy"})
