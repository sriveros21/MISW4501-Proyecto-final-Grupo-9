from ..models.training_history import TrainingHistory, TrainingHistorySchema

route_json=TrainingHistorySchema()

class GetTrainingHistory():
   def __init__(self):
      pass

   def execute(self):
      list_training=TrainingHistory.query.all()
      result=[route_json.dump(training) for training in list_training]
      return result