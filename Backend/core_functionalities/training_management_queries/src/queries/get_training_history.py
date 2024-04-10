from .base_query import BaseQuery
from ..models.database_queries import db_session_queries
from ..models.training_history import TrainingHistory, TrainingHistorySchema

route_json=TrainingHistorySchema()

class GetTrainingHistory(BaseQuery):
   def __init__(self):
      pass

   def execute(self):
      list_training=db_session_queries.query(TrainingHistory).all()
      result=[route_json.dump(training) for training in list_training]
      db_session_queries.close()
      return result