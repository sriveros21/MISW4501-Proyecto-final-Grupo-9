from flask import jsonify, request, Blueprint, Response
from ..commands.create_user import CreateUser
from ..commands.create_user_pubsub import CreateUserPubSub
# from ..commands.update_user import UpdateUser
# from ..commands.generate_token import GenerateToken
from ..queries.get_user import GetUser
from ..queries.health_user import PingCommand
# from ..commands.reset_user import ResetUserDataBase
# from ..commands.update_user_native import UpdateUserNative
# import os
from ..models.user import UserSchema
import asyncio 


user_schema = UserSchema()
users_api = Blueprint('users', __name__)


@users_api.route('/api/user/create', methods = ['POST'])
def create_user():
    json = request.get_json()
    fields_request = ['username','password','email','dni','fullName','phoneNumber']

    for field in fields_request:
        if field not in json:
            json[field]=""
    
    result = CreateUser(json['username'],json['password'],json['email'],json['dni'],json['fullName'],json['phoneNumber']).execute()    
    return jsonify(result), 201


@users_api.route('/api/user/createpubsub', methods = ['POST'])
async def create_user_ps():
    json = request.get_json()
    fields_request = ['username','password','email','dni','fullName','phoneNumber']

    for field in fields_request:
        if field not in json:
            json[field]=""
    
    # Opcion 1: Ejecutar el comando de forma sincrónica
    # Opcion 1.1: Ejecutar el comando de forma comentarios para push
    create_user_command  = CreateUserPubSub(json['username'],json['password'],json['email'],json['dni'],json['fullName'],json['phoneNumber'])    
    #return "Mensaje creado en pub/sub satisfactoriamente.", 201

        # Ejecuta el comando asincrónico y espera la respuesta
    try:
        
        response = await create_user_command.execute()
        return response, 201
    except Exception as e:
        return f"Error al crear el usuario en Pub/Sub: {e}", 500
    
    # Opcion 2: Ejecutar el comando de forma asincrónica
        # await CreateUserPubSub(json['username'],json['password'],json['email'],json['dni'],json['fullName'],json['phoneNumber']).execute2()    
        # return "Mensaje creado en pub/sub satisfactoriamente.", 201

# # 2. Actualización de usuarios
# @users_api.route('/users/<id_user>', methods = ['PATCH'])
# def update_user(id_user):
#    json = request.get_json()
#    fields_request=['status','dni','fullName','dni','phoneNumber']
#    for field in fields_request:
#        if field not in json:
#            json[field]=""

#    result = UpdateUser(json['status'],json['dni'],json['fullName'],json['phoneNumber'],id_user).execute()
#    return jsonify(result),200


# # 2. Actualización de usuarios
# @users_api.route('/users', methods = ['PATCH'])
# def update_user_native():
#    json = request.get_json()
#    fields_request=['RUV','userIdentifier','createdAt','status','score','verifyToken']
#    for field in fields_request:
#        if field not in json:
#            json[field]=""

#    result = UpdateUserNative(json['RUV'],json['userIdentifier'],json['createdAt'],json['status'],json['score'],json['verifyToken']).execute()
#    return jsonify(result),200

# # 3. Generación de token
# @users_api.route('/users/auth', methods = ['POST'])
# def generate_token():
#     json = request.get_json()
#     fields_request=['username','password']
    
#     for field in fields_request:
#         if field not in json:
#             json[field]=""

#     result = GenerateToken(json['username'],json['password']).execute()    
#     return jsonify(result),200


# 4. Consultar información del usuario
@users_api.route('/api/user/me', methods = ['GET'])
def get_user():
   token_bearer=request.headers.get('Authorization')

   if token_bearer is None:
       token=""
   else:
       token=token_bearer.replace('Bearer ', '')


   print ("El token :::> " , token) 
   result = GetUser(token).execute()
   return jsonify(result),200


# 5. Consultar salud del servicio
@users_api.route('/api/user/ping', methods = ['GET'])
def ping():
    result = PingCommand().execute()
    return jsonify({ 'result': str(result), 'status': 'OK'}), 200


# # 6. Restablecer base de datos
# @users_api.route('/users/reset', methods = ['POST'])
# def reset_database_user():
#     result = ResetUserDataBase().execute()
#     return jsonify(result),200