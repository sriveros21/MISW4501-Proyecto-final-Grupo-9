from flask import Blueprint, request, jsonify
from commands.create_event import CreateEventCommandHandler

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
