from tests.app import AppContextTestCase


class TestHealth(AppContextTestCase):

    def test_get_health(self):
        response = self.test_client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'healthy', response.data)
