from flask_sqlalchemy import SQLAlchemy
from extensions import db
from sqlalchemy.dialects.postgresql import JSON

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=True)
    fee = db.Column(db.Float, nullable=True)
    additional_info = db.Column(JSON)  # This column can store any additional JSON-structured info

    def __repr__(self):
        return f'<Event {self.name}>'
