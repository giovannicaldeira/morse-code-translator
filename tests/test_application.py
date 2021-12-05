from unittest import TestCase
from unittest.mock import MagicMock, patch

from app.application import app, socket


class ApplicationTest(TestCase):
    def setUp(self):
        self.flask_test_client = app.test_client()
        self.socket_test_client = socket.test_client(
            app, flask_test_client=self.flask_test_client
        )
        self.default_response = {'text': 'OLA MUNDO'}
    
    def test_when_I_call_index_should_be_success(self):
        r = self.flask_test_client.get('/')
        self.assertEqual(r.status_code, 200)

    @patch('app.handlers.morse.Redis')
    def test_when_I_send_a_message_should_be_success(self, redis_mock):
        redis_mock = redis_mock.return_value

        redis_mock.get = MagicMock(return_value=None)
        redis_mock.set = MagicMock(return_value=True)
        self.socket_test_client.emit('translate', {
            'text': '--- .-.. .-  -- ..- -. -.. ---'
        })
        response = self.socket_test_client.get_received()
        self.assertEqual(response[0]['args'][0], self.default_response)
