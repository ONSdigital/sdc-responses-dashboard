from datetime import datetime
from random import randint

from flask import Blueprint, jsonify

report_blueprint = Blueprint(name='reports', import_name=__name__)


# Mocked endpoint until we have database query
@report_blueprint.route('/report/<collection_exercise_id>', methods=['GET'])
def get_report(collection_exercise_id):
    sample_size = randint(0, 1000)
    accounts_created = randint(0, sample_size)
    downloads = randint(0, accounts_created)
    uploads = randint(0, downloads)

    return jsonify({
        'collectionExerciseId': collection_exercise_id,
        'details': {
            'downloads': downloads,
            'uploads': uploads,
            'accountsCreated': accounts_created,
            'sampleSize': sample_size,
            'updated': int(datetime.now().timestamp())
        }
    })
