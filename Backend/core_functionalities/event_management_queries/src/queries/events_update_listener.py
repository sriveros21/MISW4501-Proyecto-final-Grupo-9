from flask import current_app
from datetime import datetime
from kafka import KafkaConsumer
from ..models.event import Event, db
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
                'event-events',
                #bootstrap_servers=['kafka:9092'],
                bootstrap_servers=['kafka:9092'],
                auto_offset_reset='earliest',
                group_id='events-consumer',
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
                if message.value['type'] == 'UserAddedToEvent':
                    self.process_user_added(message.value)
                elif message.value['type'] == 'EventCreated':
                    self.process_event_created(message.value)

    def process_user_added(self, message):
        # Logic to update the read model based on the received message
        print(f"Processing message: {message}")
        event_id = message['event_id']
        user_id = message['user_id']
        
        event = Event.query.get(event_id)
        if not event:
            print(f"Event {event_id} not found.")
            return
        
        if "user_ids" not in event.attendees:
            event.attendees["user_ids"] = []
        
        if user_id not in event.attendees["user_ids"]:
            event.attendees["user_ids"].append(user_id)
            flag_modified(event, "attendees")
            db.session.commit()
            print(f"Added user {user_id} to event {event_id}.")

        print(f"Processing UserAddedToEvent: {message}")
    
    def process_event_created(self, message):
        print(f"Processing EventCreated: {message}")
        event_data = message['data']
        
        # Parse the event_date from string to datetime object
        if 'event_date' in event_data and isinstance(event_data['event_date'], str):
            print(f"Converting event_date to datetime object.")
            event_data['event_date'] = datetime.strptime(event_data['event_date'], '%Y-%m-%dT%H:%M:%S')
        try:
            with self.app.app_context():
                new_event = Event(**event_data)
                db.session.add(new_event)
                db.session.commit()
                print(f"Event {new_event.id} created in query service.")
        except Exception as e:
            print(f"Failed to create event in query service: {e}")
            db.session.rollback()

def start_listener_in_background(app):
    listener = EventUpdatesListener(app)
    thread = threading.Thread(target=listener.start_listening)
    thread.daemon = True  # This ensures the thread doesn't prevent the app from exiting
    thread.start()