from .base_command import BaseCommannd
from ..errors.errors import InvalidParams, EmailUsernameExist
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from ..models.database import db_session #, init_db
from ..models.user import User
# import os, requests, uuid


class CreateUser(BaseCommannd):
  def __init__(self, username, password, email, dni, fullName, phoneNumber):
    self.username=username
    self.password=password
    self.email=email
    self.dni=dni
    self.fullName=fullName
    self.phoneNumber=phoneNumber

  def execute(self):
    u = User(self.username, self.email, self.phoneNumber, self.dni, self.fullName, self.password,"POR_VERIFICAR")
    db_session.add(u)
    
    if (self.username=="" or self.email=="" or self.password=="" or self.username is None or self.email is None or self.password is None ):
      raise InvalidParams
    
    else:
      try:
        db_session.commit()
        response={"id":u.id, "createdAt":u.createdAt}
        db_session.close()
        #Funcion - Native/Verifiy.
        # CreateUser.CreateTaskVerify(self, str(u.id))

        return response
      except IntegrityError  as e:
        if isinstance(e.orig, UniqueViolation):
          db_session.close()
          raise EmailUsernameExist


  # def CreateTaskVerify(self, idUser):
  #     url_api_native=os.environ["NATIVE_PATH"]

  #     headers={'Authorization':f'Bearer {os.environ["SECRET_TOKEN"]}'}
  #     json_data = {
  #                   "transactionIdentifier": str(uuid.uuid4()),
  #                   "userIdentifier": idUser,
  #                   "userWebhook": str(os.environ["USERS_PATH"]) + "/users",
  #                         "user": {
  #                                   "email": self.email,
  #                                   "dni": self.dni,
  #                                   "fullName": self.email,
  #                                   "phone": self.phoneNumber
  #                                 }
  #                 }
      # response=requests.post(url_api_native +'/native/verify',json=json_data,headers=headers)

      if (response.status_code==201):
          return response
      else:
            return response

