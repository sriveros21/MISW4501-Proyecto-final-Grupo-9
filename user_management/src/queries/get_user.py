from ...src.commands.base_command import BaseCommannd
from ..errors.errors import NoTokenGetUser, InvalidTokenGetUser

from ..models.database import db_session
from ..models.user import User, UserSchema2

import datetime

user_schema=UserSchema2()

class GetUser(BaseCommannd):
    def __init__(self, token):
        self.token=token
        
    def execute(self):

        if self.token=="":
            raise NoTokenGetUser

        result=db_session.query(User).filter(User.token==self.token).first()
        if result is None or datetime.datetime.now() > result.expireAt:
            db_session.close()
            raise InvalidTokenGetUser
        db_session.close()
        return user_schema.dump(result)
