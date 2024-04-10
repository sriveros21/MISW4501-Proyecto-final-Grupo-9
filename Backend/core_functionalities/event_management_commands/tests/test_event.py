import os
import unittest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from src.main import create_app
from src.extensions import db

class TestEventService(TestCase):
    def create_app(self):
        os.environ['FLASK_ENV'] = 'testing'
        return create_app()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    @patch('src.commands.create_event.CreateEventCommandHandler.handle')
    def test_create_event(self, mock_handle):
        mock_handle.return_value = 1  
        response = self.client.post(url_for('event.create_event'), json={
    "name": "City Marathon 2024",
    "description": "Annual city marathon covering the downtown area with multiple categories for participants of all ages.",
    "event_date": "2024-08-22T07:00:00", 
    "duration": 5,
    "location": "Downtown City Park",
    "category": "Running",
    "fee": 50,
    "additional_info": {
        "registration_deadline": "2024-08-31",
        "max_participants": 5000,
        "min_age": 18
    }
    })
        self.assertStatus(response, 201)
        self.assertEqual(response.json['event_id'], 1)
if __name__ == '__main__':
    unittest.main()
