from datetime import datetime
from ..models.training_session import TrainingSession, db
from kafka import KafkaProducer
import json

class StartTrainingSessionCommandHandler:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=['kafka:9092'],
            value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8')
        )

    def start(self, data):
        session = TrainingSession(user_id=data['user_id'], start_time=datetime.now(), training_type=data['training_type'])
        db.session.add(session)
        db.session.commit()
        return session.id

class StopTrainingSessionCommandHandler:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=['kafka:9092'],
            value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8')
        )

    def stop(self, data):
        session = TrainingSession.query.get(data['session_id'])
        session.end_time = datetime.now()
        session.status = 'stopped'
        duration = (session.end_time - session.start_time).total_seconds()
        session.duration = duration
        db.session.commit()
        
        # Construct event data
        event_data = {
            "type": "TrainingSessionStopped",
            "data": {
                "session_id": str(session.id),
                "user_id": session.user_id,
                "end_time": session.end_time.isoformat(),
                "duration": session.duration,
                "notes": data.get('notes', '')
            }
        }
        # Publish event to Kafka
        self.producer.send('training-events', value=event_data)
        self.producer.flush()
        
        return session.id
    
class ReceiveSessionDataCommandHandler:

    def receive(self, data):
        session = TrainingSession.query.get(data['session_id'])
        if not session:
            return {"error": "Session not found"}
        # Update session with additional data
        session.power_output = data.get('power_output', 0)
        session.max_heart_rate = data.get('max_heart_rate', 0)
        session.resting_heart_rate = data.get('resting_heart_rate', 0)
        db.session.commit()
        return {"message": "Session data updated successfully"}