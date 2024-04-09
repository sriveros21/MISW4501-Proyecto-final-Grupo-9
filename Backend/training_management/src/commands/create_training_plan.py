from ..models.training_plan import TrainingPlan, db

class CreateTrainingPlanCommandHandler:
    def handle(self, data):
        plan = TrainingPlan(**data)
        db.session.add(plan)
        db.session.commit()
        return plan.id
