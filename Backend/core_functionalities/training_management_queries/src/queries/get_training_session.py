from ..models.training_session import TrainingSession

class GetTrainingSessionHandler:
    def handle(self, session_id=None):
        if session_id:
            session = TrainingSession.query.filter_by(session_id=session_id).first()
            if not session:
                return None
            session_data = {
                'id': session.id,
                'user_id': session.user_id,
                'duration': session.duration,
                'training_type': session.training_type,
                'notes': session.notes,
            }
            return session_data
        else:
            sessions = TrainingSession.query.all()
            session_data = [{
                'id': session.id,
                'user_id': session.user_id,
                'duration': session.duration,
                'training_type': session.training_type,
                'notes': session.notes,
            } for session in sessions]
            return session_data

