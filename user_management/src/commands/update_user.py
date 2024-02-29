from .base_command import BaseCommannd
from ..errors.errors import UserDoesntExist, InvalidParamsUpdate
from sqlalchemy.exc import IntegrityError
from ..models.database import db_session
from ..models.user import User

class UpdateUser(BaseCommannd):
    def __init__(self, status,dni,fullName,phoneNumber,id_user):
      self.status=status
      self.dni=dni
      self.fullName=fullName
      self.phoneNumber=phoneNumber
      self.id_user=id_user

    def execute(self):
        user=db_session.query(User).filter(User.id==self.id_user).first()

        if user is None:
            db_session.close()
            raise UserDoesntExist
        
        if (self.status=="" or self.dni=="" or self.fullName=="" or  self.phoneNumber==""):
           db_session.close()
           raise InvalidParamsUpdate
        
        user.status=self.status
        user.dni=self.dni
        user.fullName=self.fullName
        user.phoneNumber=self.phoneNumber

        try:
          db_session.commit()
         
        except IntegrityError:
          db_session.close()

        db_session.close()
        return {"msg": "el usuario ha sido actualizado"}
    