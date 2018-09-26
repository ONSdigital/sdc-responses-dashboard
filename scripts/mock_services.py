import time
from datetime import datetime
import json
from random import SystemRandom

from flask import Response, Flask
from flask_cors import CORS

app = Flask(__name__)
app.env = 'development'
CORS(app)


@app.route(
    '/reporting-api/v1/response-dashboard/<collection_instrument_type>/collection-exercise/<collection_exercise_id>',
    methods=['GET'])
def get_report(collection_instrument_type, collection_exercise_id):
    rand_gen = SystemRandom()

    sample_size = rand_gen.randint(100, 1000)
    accounts_created = rand_gen.randint(0, sample_size)
    downloads = rand_gen.randint(0, accounts_created)
    uploads = rand_gen.randint(0, downloads)
    accounts_enrolled = rand_gen.randint(uploads, accounts_created)

    if collection_instrument_type.lower() == 'seft':
        response = {
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
        }
    else:
        response = {
            'metadata': {
                'collectionExerciseId': collection_exercise_id,
                'timeUpdated': datetime.now().timestamp()
            },
            'report': {
                'inProgress': downloads - uploads,
                'accountsCreated': accounts_created,
                'accountsEnrolled': accounts_enrolled,
                'notStarted': sample_size - downloads,
                'completed': uploads,
                'sampleSize': sample_size
            }
        }
    time.sleep(5)
    return Response(json.dumps(response), content_type='application/json')


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
                    "legalBasisRef": "STA1947",
                    "surveyType": "Business"
                },
                {
                    "id": "04dbb407-4438-4f89-acc4-53445d75330c",
                    "shortName": "AOFDI",
                    "longName": "Annual Outward Foreign Direct Investment Survey",
                    "surveyRef": "063",
                    "legalBasis": "Statistics of Trade Act 1947",
                    "legalBasisRef": "STA1947",
                    "surveyType": "Business"
                },
                {
                    "id": "04dbb407-4438-4f89-acc4-53445d753111",
                    "shortName": "QBS",
                    "longName": "Quarterly Business Survey",
                    "surveyRef": "064",
                    "legalBasis": "Statistics of Trade Act 1947",
                    "legalBasisRef": "STA1947",
                    "surveyType": "Business"
                },
                {
                    "id": "56dbb407-4438-4f89-acc4-53445d753111",
                    "shortName": "LMS",
                    "longName": "Labour Market Survey",
                    "surveyRef": "999",
                    "surveyType": "Social",
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
                    "name": "Business Register an",
                    "actualExecutionDateTime": None,
                    "scheduledExecutionDateTime": "2017-09-10T23:00:00.000Z",
                    "scheduledStartDateTime": "2017-09-11T23:00:00.000Z",
                    "actualPublishDateTime": None,
                    "periodStartDateTime": "2017-05-14T23:00:00.000Z",
                    "periodEndDateTime": "2017-11-17T22:59:59.000Z",
                    "scheduledReturnDateTime": "2017-10-06T00:00:00.000Z",
                    "scheduledEndDateTime": "2018-06-29T23:00:00.000Z",
                    "executedBy": None,
                    "state": "READY_FOR_LIVE",
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
                    "exerciseRef": "201705",
                    "userDescription": "May 2017",
                    "created": None,
                    "updated": None,
                    "deleted": False,
                    "validationErrors": None
                },
                {
                    "id": "14fb3e68-4dca-46db-bf49-04b84e07e7cc",
                    "surveyId": "cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87",
                    "name": "Business Register an",
                    "actualExecutionDateTime": None,
                    "scheduledExecutionDateTime": "2017-09-10T23:00:00.000Z",
                    "scheduledStartDateTime": "2017-09-11T23:00:00.000Z",
                    "actualPublishDateTime": None,
                    "periodStartDateTime": "2017-05-14T23:00:00.000Z",
                    "periodEndDateTime": "2017-11-19T22:59:59.000Z",
                    "scheduledReturnDateTime": "2017-10-06T00:00:00.000Z",
                    "scheduledEndDateTime": "2018-06-29T23:00:00.000Z",
                    "executedBy": None,
                    "state": "LIVE",
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
                    "exerciseRef": "201709",
                    "userDescription": "September 2017",
                    "created": None,
                    "updated": None,
                    "deleted": False,
                    "validationErrors": None
                },
                {
                    "id": "14fb3e68-4dca-46db-bf49-04b84e07e777",
                    "surveyId": "cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87",
                    "name": "Business Register an",
                    "actualExecutionDateTime": None,
                    "scheduledExecutionDateTime": "2017-09-10T23:00:00.000Z",
                    "scheduledStartDateTime": "2017-09-11T23:00:00.000Z",
                    "actualPublishDateTime": None,
                    "periodStartDateTime": "2018-01-03T23:00:00.000Z",
                    "periodEndDateTime": "2018-03-17T22:59:59.000Z",
                    "scheduledReturnDateTime": "2017-10-06T00:00:00.000Z",
                    "scheduledEndDateTime": "2018-06-29T23:00:00.000Z",
                    "executedBy": None,
                    "state": "LIVE",
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
                    "exerciseRef": "201801",
                    "userDescription": "January 2018",
                    "created": None,
                    "updated": None,
                    "deleted": False,
                    "validationErrors": None
                },
                {
                    "id": "14fb3e68-4dca-46db-bf49-04b84e07e799",
                    "surveyId": "04dbb407-4438-4f89-acc4-53445d75330c",
                    "name": "Business Register an",
                    "actualExecutionDateTime": None,
                    "scheduledExecutionDateTime": "2017-09-10T23:00:00.000Z",
                    "scheduledStartDateTime": "2017-09-11T23:00:00.000Z",
                    "actualPublishDateTime": None,
                    "periodStartDateTime": "2017-09-14T23:00:00.000Z",
                    "periodEndDateTime": "2017-09-15T22:59:59.000Z",
                    "scheduledReturnDateTime": "2017-10-06T00:00:00.000Z",
                    "scheduledEndDateTime": "2018-06-29T23:00:00.000Z",
                    "executedBy": None,
                    "state": "READY_FOR_LIVE",
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
                    "exerciseRef": "201712",
                    "userDescription": "March 2017",
                    "created": None,
                    "updated": None,
                    "deleted": False,
                    "validationErrors": None
                },
                {
                    "id": "14fb3e68-4dca-46db-bf49-04b84e07e77c",
                    "surveyId": "04dbb407-4438-4f89-acc4-53445d75330c",
                    "name": "Business Register an",
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
                    "exerciseRef": "201812",
                    "userDescription": "You Can't See Me",
                    "created": None,
                    "updated": None,
                    "deleted": False,
                    "validationErrors": None
                },
                {
                    "id": "14fb3e68-4dca-46db-bf49-04b84e07e999",
                    "surveyId": "04dbb407-4438-4f89-acc4-53445d753111",
                    "name": "Quarterly Business Survey",
                    "actualExecutionDateTime": None,
                    "scheduledExecutionDateTime": "2017-09-10T23:00:00.000Z",
                    "scheduledStartDateTime": "2017-09-11T23:00:00.000Z",
                    "actualPublishDateTime": None,
                    "periodStartDateTime": "2017-09-14T23:00:00.000Z",
                    "periodEndDateTime": "2017-09-15T22:59:59.000Z",
                    "scheduledReturnDateTime": "2017-10-06T00:00:00.000Z",
                    "scheduledEndDateTime": "2018-06-29T23:00:00.000Z",
                    "executedBy": None,
                    "state": "LIVE",
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
                    "exerciseRef": "201712",
                    "userDescription": "December 2017",
                    "created": None,
                    "updated": None,
                    "deleted": False,
                    "validationErrors": None
                }
            ]
        )
    )


if __name__ == "__main__":
    app.run(host="localhost", port=5001)
