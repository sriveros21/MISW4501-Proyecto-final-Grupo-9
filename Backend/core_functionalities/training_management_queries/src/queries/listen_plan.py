from flask import current_app
from datetime import datetime
from kafka import KafkaConsumer
from ..models.training_plan import TrainingPlan, db
from sqlalchemy.orm.attributes import flag_modified
import json
import threading
import time
from kafka.errors import NoBrokersAvailable

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
                'training-plan-events',
                #bootstrap_servers=['kafka:9092'],
                bootstrap_servers=['kafka:9092'],
                auto_offset_reset='earliest',
                group_id='plan-events-consumer',
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
        # Use the stored app reference to push an application context
        with self.app.app_context():
            for message in self.consumer:
                print(f"Received message: {message}")  # Ensuring messages are received
                if message.value['type'] == 'TrainingPlanCreated':
                    self.process_plan_created(message.value)
    
    def process_plan_created(self, message):
        print(f"Processing TrainingPlanCreated: {message}")
        plan_data = message['data']
        try:
            with self.app.app_context():
                new_training_plan = TrainingPlan(**plan_data)
                db.session.add(new_training_plan)
                db.session.commit()
                print(f"Plan {new_training_plan.id} created in query service.")
        except Exception as e:
            print(f"Failed to create training plan in query service: {e}")
            db.session.rollback()

def start_listener_in_background(app):
    listener = EventUpdatesListener(app)
    thread = threading.Thread(target=listener.start_listening)
    thread.daemon = True  # This ensures the thread doesn't prevent the app from exiting
    thread.start()