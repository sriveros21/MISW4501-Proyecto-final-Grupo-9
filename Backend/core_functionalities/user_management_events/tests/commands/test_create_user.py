# from ...src.commands.create_user import CreateUser

# from  ...src.errors.errors import InvalidParams
# from ...src.commands.reset_user import ResetUserDataBase

# from ...src.models.user import User

# class TestCreateUser():

#   def test_create_user(self):
#     ResetUserDataBase().execute()
#     result=CreateUser("Alejandro2","654321","Alejandro2@hotmail.com","1030456","Alejandro Castelo","541").execute()
    
#     usuariocreado=User.query.filter_by(email="Alejandro2@hotmail.com").first()
#     ResetUserDataBase().execute()
#     resp=usuariocreado.username

#     assert resp=="Alejandro2"


#   # def test_create_user_error(self):
#   #   ResetUserDataBase().execute()
#   #   result=CreateUser("Alejandro3","","Alejandro3@hotmail.com","1030456","Alejandro","541").execute()
#   #   assert result==InvalidParams

