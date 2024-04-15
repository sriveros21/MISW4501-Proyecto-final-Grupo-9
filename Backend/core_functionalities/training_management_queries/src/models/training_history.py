from marshmallow import Schema, fields
from  sqlalchemy  import  Column, String, DateTime
from ..extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID
 

class TrainingHistory(db.Model):
    __tablename__  =  'training_history'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    date = Column(DateTime)
    username=Column(String, nullable=False)
    sport=Column(String)
    time=Column(String)
    distance=Column(String)
    weight=Column(String, nullable=False)
    intensity=Column(String)
    series=Column(String)
    calories=Column(String)


class  TrainingHistorySchema(Schema):
    id = fields.Str()
    date = fields.DateTime()
    username = fields.Str()
    sport = fields.Str()
    time = fields.Str()
    distance = fields.Str()
    weight = fields.Str()
    intensity = fields.Str()
    series = fields.Str()
    calories = fields.Str()