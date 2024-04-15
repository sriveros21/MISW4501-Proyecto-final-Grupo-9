from ..models.training_plan import TrainingPlan, db
from kafka import KafkaProducer
import json

class CreateTrainingPlanCommandHandler:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=['kafka:9092'],
            value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8')
        )

    def handle(self, data):
        plan = TrainingPlan(**data)
        db.session.add(plan)
        db.session.commit()

        event_data = {
            "type": "TrainingPlanCreated",
            "data": {
                "id": str(plan.id),
                "description": plan.description,
                "exercises": plan.exercises,
                "duration": plan.duration,
                "frequency": plan.frequency,
                "objectives": plan.objectives,
            }
        }
        self.producer.send('training-plan-events', value=event_data)
        self.producer.flush()
        return plan.id
