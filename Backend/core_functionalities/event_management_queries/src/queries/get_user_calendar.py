from ..models.event import Event

class GetUserCalendarQueryHandler:
    def __init__(self, user_id):
        self.user_id = user_id

    def execute(self):
        events = Event.query.filter(Event.attendees["user_ids"].contains([self.user_id])).all()
        print(f"Found events for user_id {self.user_id}: {events}")
        return [{
            'fecha': event.event_date.strftime('%Y-%m-%d %H:%M'),
            'nombre': event.name,
            'ubicación': event.location,
            'descripción': event.description
        } for event in events]