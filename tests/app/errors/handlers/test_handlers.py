import responses

from tests.app import AppContextTestCase


class TestErrorHandlers(AppContextTestCase):

    def test_not_found_error(self):
        response = self.test_client.get('/nonexistent-endpoint')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Oops! Not found error', response.data, )
        self.assertIn(b'Sorry, we could not find the page you were looking for.', response.data)

    @responses.activate
    def test_internal_server_error(self):

        with self.app.app_context():
            responses.add(
                responses.GET,
                self.app.config['SURVEY_URL'] + 'surveys',
                status=500)

        response = self.test_client.get('/dashboard/collection-exercise/00000000-0000-0000-0000-000000000000')

        self.assertEqual(response.status_code, 500)
        self.assertIn(b'Oops! Internal server error', response.data, )
        self.assertIn(b'Sorry, something has gone wrong.', response.data)

