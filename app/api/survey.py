from flask import Blueprint, render_template

survey_blueprint = Blueprint(name='index', import_name=__name__)


@survey_blueprint.route('/survey/<collection_exercise_id>', methods=['GET'])
def get_survey(collection_exercise_id):
    return render_template('survey.html', collex_id=collection_exercise_id)