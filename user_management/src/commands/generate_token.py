from .base_command import BaseCommannd
from ..errors.errors import InvalidUserPass, PwdUsnReq, InvalidStateUser
from sqlalchemy.exc import IntegrityError
from ..models.database import db_session
from ..models.user import User

import uuid
import datetime
import bcrypt


class GenerateToken(BaseCommannd):
    def __init__(self, username, password):
        self.username=username
        self.password=password

    def execute(self):
        if (self.username=="" or self.password=="" or self.username is None or self.password is None ):
            raise PwdUsnReq

        us=db_session.query(User).filter(User.username==self.username and User.status == "VERIFICADO").first()

        
        if us is None:
            db_session.close()
            raise InvalidUserPass
        elif us.status.name != "VERIFICADO":
            db_session.close()
            raise InvalidStateUser

        if bcrypt.checkpw(self.password.encode('utf-8'), us.password.encode('utf-8')):
            us.token=uuid.uuid4()
            us.expireAt=datetime.datetime.now()+datetime.timedelta(minutes=120)
            try:
                db_session.commit()
            except IntegrityError:
                db_session.close()
            response={"id": us.id, "token": us.token, "expireAt": us.expireAt }
            db_session.close()
            return response
        else:
            db_session.close()
            raise InvalidUserPass