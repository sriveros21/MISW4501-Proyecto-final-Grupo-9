from marshmallow import Schema, fields
from  sqlalchemy  import  Column, String, Integer, Text
from ..extensions import db
 

class TrainingPlan(db.Model):
    __tablename__  =  'training_plan'
    id = Column(Integer, primary_key=True)
    description = Column(String(255), nullable=False)
    exercises = Column(Text, nullable=False)  # This could be a JSON field
    duration = Column(String(50), nullable=False)
    frequency = Column(String(50), nullable=False)
    objectives = Column(Text, nullable=False)
    assigned_users = Column(Text, nullable=True) # This should be handle through events


class  TrainingPlanSchema(Schema):
    id = fields.Int()
    description = fields.Str()
    exercises = fields.Str()
    duration = fields.Str()
    frequency = fields.Str()
    objectives = fields.Str()
    assigned_users = fields.Str()



