from flask import Blueprint, request, jsonify
from ..commands.update_event import UpdateEventCommandHandler
from ..commands.create_event import CreateEventCommandHandler

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
    handler = UpdateEventCommandHandler()
    
    try:
        updated_event_id = handler.handle(event_id, data)
        return jsonify({"message": "Event updated successfully", "event_id": updated_event_id}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400