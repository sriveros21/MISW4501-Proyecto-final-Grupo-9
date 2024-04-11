from src.main import app
from src.models.training import User
from src.models.database import db_session

import json

class TestUsers():
   
    def test_ping(self):
        with app.test_client() as test_client:
           response=test_client.get('/users/ping')
           assert response.status_code==200

    def test_reset_database_user(self):
        with app.test_client() as test_client:
            response=test_client.post('/users/reset')
            assert response.status_code==200


    # # 1.1 Creación de usuario - cuando se crea correctamente y responde 201
    # def test_create_user_201(self):
    #     with app.test_client() as test_client:
    #        response=test_client.post(
    #            '/users',
    #            json={
    #                "username": "Alejandro",
    #                "password": "123456",
    #                "email": "Alejandro@gmail.com",
    #                "dni": "1030",
    #                "fullName": "Alejandro",
    #                "phoneNumber": "541"
    #                }
    #            )
           
    #        response_json=json.loads(response.data)
    #        assert response.status_code==201
    #        assert 'createdAt' in response_json
    #        assert 'id' in response_json
    

    # 1.2 Creación de usuario - cuando responde 400 por campos sin rellenar
    def test_create_user_400(self):
        with app.test_client() as test_client:
           response=test_client.post(
               '/users',
               json={
                   "username": "", # No esten presente en la solicitud
                   "password": "123456",
                   "email": "Alejandro@gmail.com",
                   "dni": "1030",
                   "fullName": "Alejandro",
                   "phoneNumber": "541"
                   }
               )
           
           response_json=json.loads(response.data)
           assert response.status_code==400
           assert 'Pending username, password or email fields' in response_json.values()


    # 1.3 Creación de usuario - cuando responde 400 por la ausencia de un campo (email, o password o username)
    def test_create_user_400_fied(self):
        with app.test_client() as test_client:
           response=test_client.post(
               '/users',
               json={
                   "username": "", # No esten presente en la solicitud
                   "password": "123456",
                   "dni": "1030",
                   "fullName": "Alejandro",
                   "phoneNumber": "541"
                   }
               )
           
           response_json=json.loads(response.data)
           assert response.status_code==400
           assert 'Pending username, password or email fields' in response_json.values()


    # # 1.4 Creación de usuario - cuando responde 412 porque el username o email existe 
    # def test_create_user_412(self):
    #     with app.test_client() as test_client:
    #        response=test_client.post(
    #            '/users',
    #            json={
    #                "username": "Alejandro",
    #                "password": "123456",
    #                "email": "Alejandro@gmail.com",
    #                "dni": "1030",
    #                "fullName": "Alejandro",
    #                "phoneNumber": "541"
    #                }
    #            )
           
    #        response_json=json.loads(response.data)
    #        assert response.status_code==412
    #        assert 'Email or username already exist' in response_json.values()


    # # 2.1 Actualización de usuario - cuando se actualiza correctamente y responde 200
    # def test_update_user_200(self):

    #     id_user=db_session.query(User).filter(User.email=="Alejandro@gmail.com").first()
    #     with app.test_client() as test_client:
    #        response=test_client.patch(
    #            '/users/'+ str(id_user.id),
    #            json = {
    #                     "status": "POR_VERIFICAR",
    #                     "dni": "1222222222",
    #                     "fullName": "R. Hernanedd",
    #                     "phoneNumber": "444444444"
    #                    }
    #            )
           
    #        response_json=json.loads(response.data)
    #        assert response.status_code==200
    #        assert 'el usuario ha sido actualizado' in response_json.values()


    # 3.1 Generación de token - cuando responde 200
    # def test_generate_token_200(self):
    #     with app.test_client() as test_client:
    #        response=test_client.post(
    #            '/users/auth',
    #            json={
    #                "username": "Alejandro",
    #                "password": "123456",
    #                }
    #            )
           
    #        response_json=json.loads(response.data)
    #        assert response.status_code==200
    #        assert 'expireAt' in response_json
    #        assert 'id' in response_json
    #        assert 'token' in response_json

    # 3.2 Generación de token - cuando responde 400 por un campo sin rellenar
    def test_generate_token_400(self):
        with app.test_client() as test_client:
           response=test_client.post(
               '/users/auth',
               json={
                   "username": "", # El campo no esté presente
                   "password": "123456",
                   }
               )
           
           response_json=json.loads(response.data)
           assert response.status_code==400
           assert 'mssg' in response_json
           assert 'version' in response_json

    # 3.3 Generación de token - cuando responde 400 por la ausencia de un campo
    def test_generate_token_400_field(self):
        with app.test_client() as test_client:
           response=test_client.post(
               '/users/auth',
               json={
                   "password": "123456",
                   }
               )
           
           response_json=json.loads(response.data)
           assert response.status_code==400
           assert 'mssg' in response_json
           assert 'version' in response_json

    # # 3.4 Generación de token - cuando responde 404 por credenciales erradas (password)
    # def test_generate_token_404_pass(self):
    #     with app.test_client() as test_client:
    #        response=test_client.post(
    #            '/users/auth',
    #            json={
    #                "username": "Alejandro", 
    #                "password": "1234",
    #                }
    #            )
           
    #        response_json=json.loads(response.data)
    #        assert response.status_code==404
    #        assert 'mssg' in response_json
    #        assert 'version' in response_json

    # 3.5 Generación de token - cuando responde 404 por credenciales erradas (username)
    def test_generate_token_404_user(self):
        with app.test_client() as test_client:
           response=test_client.post(
               '/users/auth',
               json={
                   "username": "Alej", 
                   "password": "1234456",
                   }
               )
           
           response_json=json.loads(response.data)
           assert response.status_code==404
           assert 'mssg' in response_json
           assert 'version' in response_json


    # 4.1 Consultar información del usuario - cuando el token es valido y responde 200
    # def test_get_user_200(self):
    #     user=db_session.query(User).filter(User.email=="Alejandro@gmail.com").first()
    #     token=user.token
    #     headers={'Authorization':f'Bearer {token}'}
    #     with app.test_client() as test_client:
    #        response=test_client.get('/users/me',json = {},headers=headers)
           
    #        response_json=json.loads(response.data)
    #        assert response.status_code==200
    #        assert 'id' in response_json
    #        assert 'username' in response_json
    #        assert 'email' in response_json
    

    # 4.2 Consultar información del usuario - token no es valido y responde 401
    def test_get_user_401(self):
        user=db_session.query(User).filter(User.email=="Alejandro@gmail.com").first()
        token="user.token"+"ab5d"
        headers={'Authorization':f'Bearer {token}'}
        with app.test_client() as test_client:
           response=test_client.get('/users/me',json = {},headers=headers)
           
           response_json=json.loads(response.data)
           assert response.status_code==401
           assert 'El token no es válido o está vencido' in response_json.values()


    # 4.3 Consultar información del usuario - token no es valido y responde 403
    def test_get_user_403(self):
        headers={}
        with app.test_client() as test_client:
           response=test_client.get('/users/me',json = {},headers=headers)
           
           response_json=json.loads(response.data)
           assert response.status_code==403
           assert 'El token no está en el encabezado de la solicitud.' in response_json.values()