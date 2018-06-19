from tests.app.app_context_test_case import AppContextTestCase


class TestReport(AppContextTestCase):

    def test_get_report(self):
        response = self.test_client.get('/report/collection-exercise/test-id')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'test-id', response.data)
        self.assertIn(b'accountsEnrolled', response.data)
        self.assertIn(b'sampleSize', response.data)
        self.assertIn(b'downloads', response.data)
        self.assertIn(b'uploads', response.data)
