from kafka import KafkaConsumer
import json
from datetime import datetime
from ..models.training_session import TrainingSession, db
from kafka.errors import NoBrokersAvailable
import time
import threading
from uuid import UUID

def json_deserializer(data):
    try:
        return json.loads(data.decode('utf-8'))
    except json.JSONDecodeError:
        print("Error decoding JSON")
        return None

def create_kafka_consumer():
    for _ in range(5):  # Retry up to 5 times
        try:
            consumer = KafkaConsumer(
                'metrics-events',
                bootstrap_servers=['kafka:9092'],
                auto_offset_reset='earliest',
                group_id='training-queries',
                value_deserializer=json_deserializer
            )
            return consumer
        except NoBrokersAvailable:
            print("Waiting for Kafka to become available...")
            time.sleep(5)  # Wait 5 seconds before retrying
    raise Exception("Failed to connect to Kafka after several attempts.")

class EventUpdatesListener():
    def __init__(self, app):
        self.app = app
        self.consumer = create_kafka_consumer()

    def start_listening(self):
        with self.app.app_context():            
            for message in self.consumer:
                if message.value and message.value['type'] == 'TrainingMetricsCalculated':
                    self.update_training_session_metrics(message.value['data'])
                    print(f"Received metrics for session {message.value['data']['session_id']}")

    def update_training_session_metrics(self, data):
        try:
            session_id = data['session_id']
            uuid_session_id = UUID(session_id)  # Ensuring the session_id is a valid UUID
            session = TrainingSession.query.filter_by(session_id=uuid_session_id).first()  # Corrected line
            if session:
                session.ftp = data['ftp']
                session.vo2max = data['vo2max']
                db.session.commit()
                print(f"Updated session {session.id} with FTP: {session.ftp}, VO2max: {session.vo2max}")
            else:
                print("Session not found")
        except ValueError:
            print("Invalid UUID format")
        except KeyError:
            print("Key error - check data keys")
        except Exception as e:
            print(f"Unexpected error: {e}")

def start_listener_in_background(app):
    listener = EventUpdatesListener(app)
    thread = threading.Thread(target=listener.start_listening)
    thread.daemon = True
    thread.start()