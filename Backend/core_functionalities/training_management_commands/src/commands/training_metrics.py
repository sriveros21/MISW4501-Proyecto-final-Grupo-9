from datetime import datetime
from ..models.training_session import TrainingSession, db
from kafka import KafkaProducer
import json

class TrainingCalculationHandler:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8')
        )
    def calculate_ftp_vo2max(self, session_id):
        # Fetch user training data
        session = TrainingSession.query.get(session_id)
        if not session:
            return {"error": "Session not found"}
        # Logic to calculate FTP and VO2max
        ftp = self._calculate_ftp(session.power_output, session.duration)
        vo2max = self._calculate_vo2max(session.max_heart_rate, session.resting_heart_rate)
        event_data = {
            "type": "TrainingMetricsCalculated",
            "data": {
                "session_id": str(session.id),
                "user_id": session.user_id,
                "ftp": ftp,
                "vo2max": vo2max,
                "timestamp": datetime.utcnow().isoformat()
            }
        }
        self.producer.send('training-metrics', value=event_data)
        self.producer.flush()

        return {"FTP": ftp, "VO2max": vo2max}


    def _calculate_ftp(self, power_output, duration):
        # Placeholder: Actual implementation needed based on data available
        return 95 * (power_output / duration)

    def _calculate_vo2max(self, max_heart_rate, resting_heart_rate):
        # Placeholder: Actual implementation needed based on data available
        return 15 * (max_heart_rate / resting_heart_rate)
