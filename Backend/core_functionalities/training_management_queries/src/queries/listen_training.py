from datetime import datetime
from kafka import KafkaConsumer
import json
from ..models.training_session import TrainingSession, db
from kafka.errors import NoBrokersAvailable
import time
import threading

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
                'event-updates',
                #bootstrap_servers=['kafka:9092'],
                bootstrap_servers=['localhost:9092'],
                auto_offset_reset='earliest',
                group_id='training-events-consumer',
                value_deserializer=json_deserializer
            )
            return consumer
        except NoBrokersAvailable:
            print("Waiting for Kafka to become available...")
            time.sleep(5)  # Wait 5 seconds before retrying
    raise Exception("Failed to connect to Kafka after several attempts.")


class EventUpdatesListener:
    def __init__(self,app):
        self.app = app
        self.consumer = create_kafka_consumer()

    def start_listening(self):
        with self.app.app_context():
            for message in self.consumer:
                print(f"Received message: {message}")  # Ensuring messages are received
                if isinstance(message.value, dict) and message.value.get('type') == 'TrainingSessionStopped':
                    self.update_query_model(message.value.get('data', {}))
                else:
                    print("Received non-compliant message or failed to deserialize:", message.value)

    def update_query_model(self, event_data):
        print("Processing data:", event_data)

        try:
            new_session = TrainingSession(
                session_id=event_data['session_id'],
                user_id=event_data['user_id'],
                end_time=datetime.fromisoformat(event_data['end_time']),
                duration=event_data['duration'],
                training_type=event_data.get('training_type', 'default'),
                calories_burned=event_data.get('calories_burned', 0),
                notes=event_data.get('notes', '')
            )
            db.session.add(new_session)
            db.session.commit()
            print("Training session updated in DB.")
        except Exception as e:
            db.session.rollback()
            print(f"Failed to update session data: {e}")

def start_listener_in_background(app):
    listener = EventUpdatesListener(app)
    thread = threading.Thread(target=listener.start_listening)
    thread.daemon = True
    thread.start()