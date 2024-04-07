from flask import jsonify, request, Blueprint, Response
from ..queries.get_training_history import GetTrainingHistory

# from ..commands.update_user import UpdateUser
# from ..commands.generate_token import GenerateToken
# from ..queries.get_user import GetUser
# from ..queries.health_user import PingCommand
# from ..commands.reset_user import ResetUserDataBase
# from ..commands.update_user_native import UpdateUserNative
# import os
from ..models.training_history import TrainingHistorySchema
# import asyncio 


training_history_schema = TrainingHistorySchema()
training_api = Blueprint('training', __name__)


@training_api.route('/api/training/history', methods = ['GET'])
def get_training_history():
#    token_bearer=request.headers.get('Authorization')

#    if token_bearer is None:
#        token=""
#    else:
#        token=token_bearer.replace('Bearer ', '')

   result = GetTrainingHistory().execute()
   return jsonify(result),200


# @training_api.route('/api/training/ping', methods = ['GET'])
# def ping():
#     result = PingCommand().execute()
#     return jsonify({ 'result': str(result), 'status': 'OK'}), 200


# # 6. Restablecer base de datos
# @users_api.route('/users/reset', methods = ['POST'])
# def reset_database_user():
#     result = ResetUserDataBase().execute()
#     return jsonify(result),200