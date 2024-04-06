from flask import Blueprint, request, jsonify
from commands.create_event import CreateEventCommandHandler
from models.event import Event, db
from datetime import datetime

event_blueprint = Blueprint('event', __name__)

@event_blueprint.route('/events', methods=['POST'])
def create_event():
    data = request.json
    handler = CreateEventCommandHandler()
    try:
        event_id = handler.handle(data)
        return jsonify({"message": "Event created successfully", "event_id": event_id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@event_blueprint.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.json
    handler = CreateEventCommandHandler()
    
    event = Event.query.get(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    # Check if the event start date has already passed
    if datetime.now() >= event.event_date:
        return jsonify({"error": "Cannot edit past events"}), 400

    try:
        handler.validate_data(data)  # Validate mandatory fields
        if 'event_date' in data:
            if isinstance(data['event_date'], str):
                data['event_date'] = datetime.strptime(data['event_date'], '%Y-%m-%dT%H:%M:%S')
        handler.check_overlap(data, event_id)  # Check for overlapping events

        # Update event attributes
        for key, value in data.items():
            setattr(event, key, value)
        
        db.session.commit()
        return jsonify({"message": "Event updated successfully", "event_id": event.id}), 200
    except ValueError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400