from flask import Blueprint, request, jsonify
from datetime import datetime
from ..commands.training_session import StartTrainingSessionCommandHandler, StopTrainingSessionCommandHandler, ReceiveSessionDataCommandHandler

training_session_blueprint = Blueprint('training_session', __name__)

@training_session_blueprint.route('/start-training', methods=['POST'])
def start_training_session():
    data = request.json
    handler = StartTrainingSessionCommandHandler()
    session_id = handler.start(data)
    return jsonify({"session_id": session_id}), 201

@training_session_blueprint.route('/stop-training', methods=['POST'])
def stop_training_session():
    data = request.json
    handler = StopTrainingSessionCommandHandler()
    session_id = handler.stop(data)
    return jsonify({"message": "Training session stopped successfully", "session_id": session_id}), 200

@training_session_blueprint.route('/receive_session-data', methods=['POST'])
def submit_session_data():
    data = request.json
    handler = ReceiveSessionDataCommandHandler()
    results = handler.receive(data)
    return jsonify(results), 200