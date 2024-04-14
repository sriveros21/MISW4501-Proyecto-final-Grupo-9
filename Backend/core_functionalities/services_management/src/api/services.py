from flask import Blueprint, request, jsonify
from ..queries.get_services import get_services_and_events
from ..commands.add_service import add_service

service_blueprint = Blueprint('service', __name__)

@service_blueprint.route('/services', methods=['GET'])
def get_services():
    services, events = get_services_and_events()
    return jsonify({
        'services': [s.serialize() for s in services],
        'events': events
    })

@service_blueprint.route('/services', methods=['POST'])
def create_service():
    data = request.json
    service_id = add_service(data)
    return jsonify({"message": "Service added successfully", "service_id": service_id}), 201
