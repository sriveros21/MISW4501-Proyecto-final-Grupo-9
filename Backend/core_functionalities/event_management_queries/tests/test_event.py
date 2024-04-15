import unittest
from src.config import TestingConfig
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from src.main import create_app
from src.extensions import db

class TestEventService(TestCase):
    def create_app(self):
        return create_app(TestingConfig)

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @patch('src.queries.get_event.GetEventQueryHandler.handle')
    def test_get_event(self, mock_handle):
        mock_handle.return_value = {'id': 1, 'name': 'Sample Event'}
        response = self.client.get(url_for('event.get_event', event_id=1))
        self.assert200(response)
        self.assertEqual(response.json['name'], 'Sample Event')
if __name__ == '__main__':
    unittest.main()
