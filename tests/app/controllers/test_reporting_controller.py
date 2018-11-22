import responses

from app.controllers.reporting_controller import get_reporting_details
from tests.app import AppContextTestCase


class TestReportingController(AppContextTestCase):
    reporting_response = {'metadata': {'collectionExerciseId': '14fb3e68-4dca-46db-bf49-04b84e07e999',
                                       'timeUpdated': 1533895381.534031},
                          'report': {'inProgress': 99, 'accountsPending': 402, 'accountsEnrolled': 259,
                                     'notStarted': 457, 'completed': 160, 'sampleSize': 716}}

    @responses.activate
    def test_get_reporting_details_success(self):
        with self.app.app_context():
            responses.add(responses.GET, self.app.config['REPORTING_URL'] + '/reporting-api/v1/response-dashboard'
                                                                            '/survey'
                                                                            '/57586798-74e3-49fd-93da-a782ec5f5129'
                                                                            '/collection-exercise'
                                                                            '/14fb3e68-4dca-46db-bf49'
                                                                            '-04b84e07e999',
                          json=self.reporting_response, status=200)

            report = get_reporting_details('57586798-74e3-49fd-93da-a782ec5f5129',
                                           '14fb3e68-4dca-46db-bf49-04b84e07e999')

        self.assertEqual(report, self.reporting_response)
