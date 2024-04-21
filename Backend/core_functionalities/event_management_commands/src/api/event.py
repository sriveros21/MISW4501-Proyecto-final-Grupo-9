from flask import Blueprint, request, jsonify

from ..commands.add_user_to_event import AddUserToEventCommand
from ..commands.update_event import UpdateEventCommandHandler
from ..commands.create_event import CreateEventCommandHandler
from ..commands.publish_event import PublishEventCommandHandler

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

@event_blueprint.route('/events/<int:event_id>/publish', methods=['POST'])
def publish_event(event_id):
    handler = PublishEventCommandHandler()
    try:
        handler.handle(event_id)
        return jsonify({"message": "Event published successfully"}), 200
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
    
@event_blueprint.route('/events/<int:event_id>/add', methods=['POST'])
def add_user(event_id):
    user_id = request.json.get('user_id')
    try:
        command = AddUserToEventCommand(user_id=user_id, event_id=event_id)
        command.execute()
        return jsonify({"message": "User added successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404