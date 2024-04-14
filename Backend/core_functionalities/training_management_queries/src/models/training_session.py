from  sqlalchemy  import  Column, String, DateTime, Integer, Float
from ..extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID
 

class TrainingSession(db.Model):
    __tablename__  =  'training_session'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    user_id=Column(Integer, nullable=False)
    end_time=Column(DateTime)
    duration=Column(String)
    notes=Column(String)
    calories_burned=Column(String)
    training_type=Column(String)
    ftp = Column(Float)
    vo2max = Column(Float)

    def __repr__(self):
        return f'<TrainingSession {self.id}>'