from ..models.event import Event

class GetEventQueryHandler:
    def handle(self, event_id):
        event = Event.query.get(event_id)
        if not event:
            return None

        event_data = {
            'id': event.id,
            'name': event.name,
            'description': event.description,
            'event_date': event.event_date.strftime('%Y-%m-%dT%H:%M:%S'),
            'duration': event.duration,
            'location': event.location,
            'category': event.category,
            'fee': event.fee,
            'additional_info': event.additional_info
        }
        return event_data