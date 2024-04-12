from flask import Blueprint, request, jsonify
from ..commands.training_metrics import TrainingCalculationHandler

training_metrics_blueprint = Blueprint('training_metrics', __name__)

@training_metrics_blueprint.route('/calculate-ftp-vo2max', methods=['POST'])
def calculate_ftp_vo2max():
    session_id = request.json.get('session_id')
    handler = TrainingCalculationHandler()
    results = handler.calculate_ftp_vo2max(session_id)
    return jsonify(results), 200