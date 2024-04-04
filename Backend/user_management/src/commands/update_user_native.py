from .base_command import BaseCommannd
from ..errors.errors import UserDoesntExist, InvalidParamsUpdate
#from .send_mail import send_approved_mail
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from ..models.database import db_session
from ..models.user import User
import os, requests
from flask import jsonify

class UpdateUserNative(BaseCommannd):
    def __init__(self, RUV,userIdentifier,createdAt,status,score,verifyToken):
      self.status=status
      self.RUV = RUV
      self.createdAt = createdAt
      self.score = score
      self.verifyToken = verifyToken
      self.id_user = userIdentifier

    def execute(self):
        user=db_session.query(User).filter(User.id==self.id_user).first()

        if user is None:
            db_session.close()
            raise UserDoesntExist
        
        user.status=self.status
        user.updatedAt = datetime.now()
        
         #Consumir FUNCIÓN de enviar email con los datos traidos desde TRUENATIVE.
        UpdateUserNative.SendMailNotification(self, self.RUV, self.status, user.id, user.fullName, user.phoneNumber, user.email)
        try:
            db_session.commit()
        except IntegrityError:
          db_session.close()

        db_session.close()
        return {"msg": "el usuario ha sido actualizado"}


    def SendMailNotification(self, RUV, status, userId, fullName, phoneNumber, email):
        url_funcion_mail=os.environ["MAIL_PATH"]
        
        # mensaje_html = {
        #             "Detalles del resultado": 
        #             {
        #                 "RUV": str(RUV),
        #                 "Estado": status,
        #                 "UserId": str(userId),
        #                 "Nombre": fullName,
        #                 "Telefono": phoneNumber
        #             }
        #         }

        mensaje_html = f'''<body><h1>Detalles del resultado</h1><table border="1"><tr><td>Dato</td><td>Resultado</td></tr><tr><td>RUV</td><td>{RUV}</td></tr><tr><td>Estado</td><td>{status}</td></tr><tr><td>UserId</td><td>{userId}</td></tr><tr><td>Nombre</td><td>{fullName}</td></tr><tr><td>Telefono</td><td>{phoneNumber}</td></tr></table></body>'''

        json_data = {"mail_destino": email, "mensaje": mensaje_html,"asunto": "Notificación."}

        print("Data", str(json_data))
        response=requests.post(url_funcion_mail,json=json_data)

        if (response.status_code==201):
            return response
        else:
            return response
