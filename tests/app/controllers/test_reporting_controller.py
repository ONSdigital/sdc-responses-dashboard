import json

import responses

from app.controllers.reporting_controller import get_reporting_details
from tests.app import AppContextTestCase


class TestReportingController(AppContextTestCase):

    reporting_response = {'metadata': {'collectionExerciseId': '14fb3e68-4dca-46db-bf49-04b84e07e999',
                                       'timeUpdated': 1533895381.534031},
                          'report': {'inProgress': 99, 'accountsCreated': 402, 'accountsEnrolled': 259,
                                     'notStarted': 457, 'completed': 160, 'sampleSize': 716}}

    @responses.activate
    def test_get_reporting_details_success(self):
        with self.app.app_context():
            responses.add(responses.GET, self.app.config['REPORTING_URL'] + '/reporting-api/v1/response-dashboard'
                                                                            '/seft/'
                                                                            'collection-exercise'
                                                                            '/14fb3e68-4dca-46db-bf49'
                                                                            '-04b84e07e999',
                                                                            json=self.reporting_response, status=200)

            report = get_reporting_details('seft', '14fb3e68-4dca-46db-bf49-04b84e07e999')
            decoded_report = json.loads(report)

        self.assertEqual(decoded_report, self.reporting_response)

