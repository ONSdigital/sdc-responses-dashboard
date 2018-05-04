from datetime import datetime
import json
from random import randint

from flask import Blueprint, Response

report_blueprint = Blueprint(name='reports', import_name=__name__)


# Mocked endpoint until we have database query
@report_blueprint.route('/report/<collection_exercise_id>', methods=['GET'])
def get_report(collection_exercise_id):
    sample_size = randint(100, 1000)
    accounts_created = randint(0, sample_size)
    downloads = randint(0, accounts_created)
    uploads = randint(0, downloads)

    return Response(
        json.dumps({
            'metadata': {
                'collectionExerciseId': collection_exercise_id,
                'timeUpdated': int(datetime.now().timestamp())
            },
            'report': {
                'downloads': downloads,
                'uploads': uploads,
                'accountsCreated': accounts_created,
                'sampleSize': sample_size
            }
        }),
        content_type='application/json')
