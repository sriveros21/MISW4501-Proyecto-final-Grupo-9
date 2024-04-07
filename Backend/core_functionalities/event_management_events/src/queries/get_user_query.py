# from ..queries.base_queries import BaseQueries
# from ..errors.errors import NoTokenGetUser, InvalidTokenGetUser

# from ..models.database import db_session
# from ..models.database_queries import db_session_queries
# from ..models.user import User, UserSchema2

# import datetime

# user_schema=UserSchema2()

# class GetUser(BaseQueries):
#     def __init__(self, token):
#         self.token=token
        
#     def execute(self):

#         if self.token=="":
#             raise NoTokenGetUser

#         result=db_session_queries.query(User).filter(User.id==self.token).first()
#         # if result is None or datetime.datetime.now() > result.expireAt:
#         #     db_session_queries.close()
#         #     raise InvalidTokenGetUser
#         db_session_queries.close()
#         return user_schema.dump(result)
