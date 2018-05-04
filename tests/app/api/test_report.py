from tests.app.app_context_test_case import AppContextTestCase


class TestReport(AppContextTestCase):

    def test_get_report(self):
        response = self.test_client.get('/report/collection_exercise_id')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'collection_exercise_id', response.data)
        self.assertIn(b'accountsCreated', response.data)
        self.assertIn(b'sampleSize', response.data)
        self.assertIn(b'downloads', response.data)
        self.assertIn(b'uploads', response.data)
