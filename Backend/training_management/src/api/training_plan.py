from flask import Blueprint, request, jsonify
from commands.create_training_plan import CreateTrainingPlanCommandHandler
from queries.get_training_plan import GetTrainingPlanQueryHandler
import json

training_plan_blueprint = Blueprint('training_plan', __name__)

@training_plan_blueprint.route('/training-plan', methods=['POST'])
def create_training_plan():
    data = request.json
    data['assigned_users'] = json.dumps(data.get('assigned_users', []))
    handler = CreateTrainingPlanCommandHandler()
    training_plan_id = handler.handle(data)
    return jsonify({ "id": training_plan_id }), 201

@training_plan_blueprint.route('/training-plan/<int:plan_id>', methods=['GET'])
def get_training_plan(plan_id):
    handler = GetTrainingPlanQueryHandler()
    plan = handler.handle(plan_id)
    return jsonify(plan), 200

@training_plan_blueprint.route('/training-plans', methods=['GET'])
def get_training_plans():
    handler = GetTrainingPlanQueryHandler()
    plans = handler.handleAll()
    return jsonify(plans), 200

