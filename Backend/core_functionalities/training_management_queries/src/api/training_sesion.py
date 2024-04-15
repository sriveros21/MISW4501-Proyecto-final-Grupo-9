from flask import jsonify, Blueprint
from ..queries.get_training_session import GetTrainingSessionHandler


training_session_blueprint = Blueprint('training_session', __name__)


@training_session_blueprint.route('/training-sessions', methods = ['GET'])
def get_all_training_sessions():
   handler = GetTrainingSessionHandler()
   sessions = handler.handle()
   return jsonify(sessions),200


@training_session_blueprint.route('/training-sessions/<uuid:session_id>', methods=['GET'])
def get_training_session(session_id):
    handler = GetTrainingSessionHandler()
    session = handler.handle(session_id)
    return jsonify(session), 200