from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TrainingPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    exercises = db.Column(db.Text, nullable=False)  # This could be a JSON field
    duration = db.Column(db.String(50), nullable=False)
    frequency = db.Column(db.String(50), nullable=False)
    objectives = db.Column(db.Text, nullable=False)
    # Pending evaluate relationships, e.g., to users or to other entities
