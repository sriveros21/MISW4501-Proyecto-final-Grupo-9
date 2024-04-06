from flask_sqlalchemy import SQLAlchemy
from extensions import db

class TrainingPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    exercises = db.Column(db.Text, nullable=False)  # This could be a JSON field
    duration = db.Column(db.String(50), nullable=False)
    frequency = db.Column(db.String(50), nullable=False)
    objectives = db.Column(db.Text, nullable=False)
    assigned_users = db.Column(db.Text, nullable=True) # This should be handle through events
