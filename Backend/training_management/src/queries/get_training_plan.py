from models.training_plan import TrainingPlan

class GetTrainingPlanQueryHandler:
    def handle(self, plan_id):
        plan = TrainingPlan.query.filter_by(id=plan_id).first()
        return {
            "id": plan.id,
            "description": plan.description,
            "exercises": plan.exercises,
            "duration": plan.duration,
            "frequency": plan.frequency,
            "objectives": plan.objectives
        }

    def handleAll(self):
        plans = TrainingPlan.query.all()
        return [{
            "id": plan.id,
            "description": plan.description,
            "exercises": plan.exercises,
            "duration": plan.duration,
            "frequency": plan.frequency,
            "objectives": plan.objectives
        } for plan in plans]