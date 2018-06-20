from datetime import datetime
import json
from random import randint

from flask import Response, Flask
from flask_cors import CORS

app = Flask(__name__)
app.env = 'development'
CORS(app)


@app.route('/reporting-api/v1/response-dashboard/collection_exercise/<collection_exercise_id>', methods=['GET'])
def get_report(collection_exercise_id):
    sample_size = randint(100, 1000)
    accounts_created = randint(0, sample_size)
    downloads = randint(0, accounts_created)
    uploads = randint(0, downloads)

    return Response(
        json.dumps({
            'metadata': {
                'collectionExerciseId': collection_exercise_id,
                'timeUpdated': datetime.now().timestamp()
            },
            'report': {
                'downloads': downloads,
                'uploads': uploads,
                'accountsEnrolled': accounts_created,
                'sampleSize': sample_size
            }
        }),
        content_type='application/json')


@app.route('/surveys', methods=['GET'])
def get_surveys():
    return Response(
        json.dumps(
            [
                {
                    "id": "cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87",
                    "shortName": "BRES",
                    "longName": "Business Register and Employment Survey",
                    "surveyRef": "221",
                    "legalBasis": "Statistics of Trade Act 1947",
                    "legalBasisRef": "STA1947"
                },
                {
                    "id": "04dbb407-4438-4f89-acc4-53445d75330c",
                    "shortName": "AOFDI",
                    "longName": "Annual Outward Foreign Direct Investment Survey",
                    "surveyRef": "063",
                    "legalBasis": "Statistics of Trade Act 1947",
                    "legalBasisRef": "STA1947"
                }
            ]
        )
    )


@app.route('/collectionexercises', methods=['GET'])
def get_collection_exercises():
    return Response(
        json.dumps(
            [
                {
                    "id": "14fb3e68-4dca-46db-bf49-04b84e07e77c",
                    "surveyId": "cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87",
                    "name": "BRES_2017",
                    "actualExecutionDateTime": None,
                    "scheduledExecutionDateTime": "2017-09-10T23:00:00.000Z",
                    "scheduledStartDateTime": "2017-09-11T23:00:00.000Z",
                    "actualPublishDateTime": None,
                    "periodStartDateTime": "2017-09-14T23:00:00.000Z",
                    "periodEndDateTime": "2017-09-15T22:59:59.000Z",
                    "scheduledReturnDateTime": "2017-10-06T00:00:00.000Z",
                    "scheduledEndDateTime": "2018-06-29T23:00:00.000Z",
                    "executedBy": None,
                    "state": "CREATED",
                    "caseTypes": [
                        {
                            "actionPlanId": "e71002ac-3575-47eb-b87f-cd9db92bf9a7",
                            "sampleUnitType": "B"
                        },
                        {
                            "actionPlanId": "0009e978-0932-463b-a2a1-b45cb3ffcb2a",
                            "sampleUnitType": "BI"
                        }
                    ],
                    "exerciseRef": "221_201712",
                    "userDescription": None,
                    "created": None,
                    "updated": None,
                    "deleted": False,
                    "validationErrors": None
                }
            ]
        )
    )


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
