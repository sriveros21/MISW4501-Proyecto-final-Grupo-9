from models.training_plan import TrainingPlan

class GetTrainingPlanQueryHandler:
    def handle(self, plan_id):
        plan = TrainingPlan.query.filter_by(id=plan_id).first()
        return {
            "id": plan.id,
            "name": plan.name,
            "exercises": plan.exercises,
            "duration": plan.duration,
            "frequency": plan.frequency,
            "objectives": plan.objectives
        }