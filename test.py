import json
import unittest

import app


class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def test_hello_world(self):
        response = self.app.get('/')

        assert response.status_code == 200
        assert response.get_data(as_text=True) == 'Hello, world!'


class TestSubmission(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def test_contact_submission(self):
        payload = {
            'first_name': 'Hazel',
            'last_name': 'Wright',
            'email': 'test@hazelsarahwright.com',
            'message': 'test message'
        }

        response = self.app.post(
            '/submissions',
            data=json.dumps(payload),
            content_type='application/json'
        )

        assert response.status_code == 201
        response_data = json.loads(response.get_data())
        
        for item in ['id', 'first_name', 'last_name', 'email', 'message']:
            assert item in response_data['submission']


if __name__ == '__main__':
    unittest.main()
