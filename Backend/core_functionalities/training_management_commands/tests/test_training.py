import os
import sys
import unittest
from flask import json
from src.main import create_app
from src.extensions import db
from src.config import TestingConfig

class TrainingPlanTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """Teardown all initialized variables."""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_training_plan(self):
        """Test API can create a training plan (POST request)"""
        # Mock the CreateTrainingPlanCommandHandler here if necessary
        plan = {'objectives': 'New Training Plan', 'description': 'This is a test plan.','exercises': 'This is a test plan.','frequency': 'This is a test plan.','duration': 'This is a test plan.'}
        response = self.client().post('/training-plan', json=plan)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', json.loads(response.data).keys())

    def test_get_training_plan(self):
        """Test API can get a specific training plan (GET request)."""
        # Mock the GetTrainingPlanQueryHandler here if necessary
        # Assuming there's a plan with ID 1
        response = self.client().get('/training-plan/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('name', json.loads(response.data).keys())

    def test_create_training_plan(self):
        pass

    def test_get_training_plan(self):
        pass

if __name__ == "__main__":
    unittest.main()