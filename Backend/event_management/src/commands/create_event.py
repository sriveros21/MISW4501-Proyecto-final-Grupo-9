from models.event import Event, db
from datetime import datetime
from sqlalchemy.exc import IntegrityError

class CreateEventCommandHandler:
    def handle(self, data):
        # Parse the event_date string to datetime object
        if 'event_date' in data:
            data['event_date'] = datetime.strptime(data['event_date'], '%Y-%m-%dT%H:%M:%S')

        try:
            event = Event(**data)
            db.session.add(event)
            db.session.commit()
            return event.id
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Event data is invalid or overlaps with an existing event.")