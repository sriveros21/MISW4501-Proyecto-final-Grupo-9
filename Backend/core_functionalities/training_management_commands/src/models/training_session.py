from flask_sqlalchemy import SQLAlchemy
from ..extensions import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class TrainingSession(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime)
    training_type = db.Column(db.String(255), default='default')
    calories_burned = db.Column(db.Float)
    duration = db.Column(db.Float)
    ftp = db.Column(db.Float)
    vo2max = db.Column(db.Float)
    power_output = db.Column(db.Float)
    max_heart_rate = db.Column(db.Integer)
    resting_heart_rate = db.Column(db.Integer) 