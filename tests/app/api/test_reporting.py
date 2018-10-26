import json

import responses
from requests import HTTPError

from app.api.reporting import reporting_details
from tests.app import AppContextTestCase


class TestReporting(AppContextTestCase):

    reporting_response = {'metadata': {'collectionExerciseId': '14fb3e68-4dca-46db-bf49-04b84e07e999',
                                       'timeUpdated': 1533895381.534031},
                          'report': {'inProgress': 99, 'accountsPending': 402, 'accountsEnrolled': 259,
                                     'notStarted': 457, 'completed': 160, 'sampleSize': 716}}

    @responses.activate
    def test_reporting_details_success(self):
        with self.app.app_context():
            responses.add(responses.GET, self.app.config['REPORTING_URL'] + '/reporting-api/v1/response-dashboard'
                                                                            '/seft/'
                                                                            'collection-exercise'
                                                                            '/14fb3e68-4dca-46db-bf49'
                                                                            '-04b84e07e999',
                                                                            json=self.reporting_response, status=200)

            report = reporting_details('seft', '14fb3e68-4dca-46db-bf49-04b84e07e999')
            decoded_report = json.loads(report)

        self.assertEqual(decoded_report, self.reporting_response)

    @responses.activate
    def test_reporting_details_malformed_collex(self):

        response = self.test_client.get('/dashboard/reporting/eq/collection-exercise/0002133304032532504')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Sorry, we could not find the page you were looking for.', response.data)

    @responses.activate
    def test_reporting_details_invalid_CI_type(self):

        response = self.test_client.get('/dashboard/reporting/SAFT/collection-exercise/14fb3e68-4dca-46db-bf49-04b84e07e999')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Sorry, we could not find the page you were looking for.', response.data)

    @responses.activate
    def test_reporting_details_invalid_collex(self):
        with self.app.app_context():
            responses.add(responses.GET, self.app.config['REPORTING_URL'] + '/reporting-api/v1/response-dashboard'
                                                                            '/seft/'
                                                                            'collection-exercise'
                                                                            '/14fb3e68-4dca-46db-bf49'
                                                                            '-04b84e07e997',
                                                                            status=404)
        response = self.test_client.get('/dashboard/reporting/seft/collection-exercise/14fb3e68-4dca-46db-bf49-04b84e07e997')
        self.assertEqual(response.status_code, 404)
