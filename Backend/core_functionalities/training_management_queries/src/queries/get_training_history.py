from .base_query import BaseQuery

# from ..errors.errors import InvalidSearch, NoToken, InvalidToken
from ..models.database_queries import db_session_queries
from ..models.training_history import TrainingHistory, TrainingHistorySchema

# import os
# import requests


route_json=TrainingHistorySchema()

class GetTrainingHistory(BaseQuery):
   def __init__(self):
      # self.token=token
      pass

   def execute(self):
       
    #   #Validación del tocket, Consumiendo el servicio de validación
    #   if self.token=="":
    #      raise NoToken
      
    #   url_api_user=os.environ["USERS_PATH"]

    #   headers={'Authorization':f'Bearer {self.token}'}
    #   response=requests.get(url_api_user +'/users/me',json={},headers=headers)
    #   #assert response.status_code==200

    #   if response.status_code!=200:
    #      raise InvalidToken

    #   # --------------------------------------------------

      list_training=db_session_queries.query(TrainingHistory).all()
      result=[route_json.dump(training) for training in list_training]
      db_session_queries.close()
      return result