from .base_command import BaseCommannd
from sqlalchemy import MetaData, Table

from ..models.database import engine, init_db

class ResetUserDataBase(BaseCommannd):
    def execute(self):
        metadata=MetaData()
        my_table=Table('user',metadata)
        my_table.drop(engine)
        init_db()
        return {"msg":"Todos los datos fueron eliminados"}

 
