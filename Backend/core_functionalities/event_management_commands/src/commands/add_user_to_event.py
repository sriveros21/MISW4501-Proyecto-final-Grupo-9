from ..models.event import Event, db
from sqlalchemy.orm.attributes import flag_modified
from kafka import KafkaProducer
import json

class AddUserToEventCommand:
    def __init__(self, user_id, event_id):
        self.user_id = user_id
        self.event_id = event_id
        self.producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def execute(self):
        event = Event.query.get(self.event_id)
        if not event:
            raise ValueError("Event not found")
        if "user_ids" not in event.attendees:
            print("attendees not in event")
            event.attendees["user_ids"] = []
        if self.user_id not in event.attendees["user_ids"]:
            print("user not in attendees")
            event.attendees["user_ids"].append(self.user_id)
            flag_modified(event, "attendees")
            db.session.commit()
            # Publish an event to Kafka after updating the database
            message = {"event_id": self.event_id, "user_id": self.user_id, "type": "UserAddedToEvent"}
            self.producer.send('event-updates', value=message)
            self.producer.flush()