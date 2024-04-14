from flask import Blueprint, request, jsonify
from ..commands.create_training_plan import CreateTrainingPlanCommandHandler

training_plan_blueprint = Blueprint('training_plan', __name__)

@training_plan_blueprint.route('/training-plan', methods=['POST'])
def create_training_plan():
    data = request.json
    handler = CreateTrainingPlanCommandHandler()
    training_plan_id = handler.handle(data)
    return jsonify({ "id": training_plan_id }), 201
