from .base_command import BaseCommannd
from ..errors.errors import InvalidParams, EmailUsernameExist
from google.cloud import pubsub_v1  # Importa la biblioteca cliente de Pub/Sub
import asyncio, datetime, os

# Define la clase CreateUser
class CreateUserPubSub(BaseCommannd):
    def __init__(self, username, password, email, dni, fullName, phoneNumber):
        self.username = username
        self.password = password
        self.email = email
        self.dni = dni
        self.fullName = fullName
        self.phoneNumber = phoneNumber

    async def execute(self):
        # Crea un cliente de Pub/Sub
        print(f"Iniciando execute....")
        try:

            # Ruta al archivo de credenciales relativa a la raíz del proyecto
            credentials_path = "credentials.json"

            # Obteniendo la ruta completa del archivo
            full_credentials_path = os.path.abspath(credentials_path)

            # Configurando las credenciales
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = full_credentials_path

            publisher = pubsub_v1.PublisherClient()
            topic_path = publisher.topic_path('proyecto-final-miso-416801', 'registrar-usuario')
            # Crea un mensaje con los datos del usuario
            message_data = {
                'username': self.username,
                'password': self.password,
                'email': self.email,
                'dni': self.dni,
                'fullName': self.fullName,
                'phoneNumber': self.phoneNumber
            }
        
        # Publica el mensaje en el tema de Pub/Sub
        # registrarUsuario = publisher.publish(topic_path, data=str(message_data).encode('utf-8'))

        
            # Espera a que se complete la publicación del mensaje

            # print(f"Vamos a publicar....")

            # message_id = await publisher.publish(topic_path, data=str(message_data).encode('utf-8'))
            # # print("Mensaje publicado correctamente en Pub/Sub")

            # #future = publisher.publish(topic_path, data=str(message_data).encode('utf-8'))
            # # Espera a que se complete la publicación del mensaje
            # #message_id = await future
            # print(f"Mensaje publicado correctamente en Pub/Sub con ID: {message_id}")

            # # await registrarUsuario
            # # print("Mensaje publicado correctamente en Pub/Sub")

            # # Lógica para el resto del comando CreateUser
            # # Por ejemplo, aquí podrías agregar la lógica para crear el usuario en la base de datos
            # # ...
            
            # #response={"Mensaje":"Mensaje publicado correctamente en Pub/Sub"}
            # response={"Msg":"Mensaje creado satisfactoriamente en PUB/SUB", "createdAt":datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            # return response
        

            # Publica el mensaje en el tema de Pub/Sub
            print(f"Vamos a publicar....")

            future = publisher.publish(topic_path, data=str(message_data).encode('utf-8'))
            print(f"se creo el publish.....")
            #message_id = await future
            message_id = await asyncio.wrap_future(future)

            print(f"Mensaje publicado correctamente en Pub/Sub con ID: {message_id}")

            # Preparar la respuesta
            response = {
                "Msg": "Mensaje creado satisfactoriamente en PUB/SUB",
                "createdAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            return response
        
        except Exception as e:
            print(f"Error al publicar mensaje en Pub/Sub: {e}")
            # Maneja el error adecuadamente, por ejemplo, lanzando una excepción
            raise Exception("Error al publicar mensaje en Pub/Sub")


    async def execute2(self):
          # Crea un cliente de Pub/Sub
        print(f"Iniciando execute 2....")
        try:

            # Ruta al archivo de credenciales relativa a la raíz del proyecto
            credentials_path = "credentials.json"

            # Obteniendo la ruta completa del archivo
            full_credentials_path = os.path.abspath(credentials_path)

            # Configurando las credenciales
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = full_credentials_path

            publisher = pubsub_v1.PublisherClient()
            topic_path = publisher.topic_path('proyecto-final-miso-416801', 'registrar-usuario')
            # Crea un mensaje con los datos del usuario
            message_data = {
                'username': self.username,
                'password': self.password,
                'email': self.email,
                'dni': self.dni,
                'fullName': self.fullName,
                'phoneNumber': self.phoneNumber
            }
        
        # Publica el mensaje en el tema de Pub/Sub
        # registrarUsuario = publisher.publish(topic_path, data=str(message_data).encode('utf-8'))

        
            # Espera a que se complete la publicación del mensaje

            # print(f"Vamos a publicar....")

            # message_id = await publisher.publish(topic_path, data=str(message_data).encode('utf-8'))
            # # print("Mensaje publicado correctamente en Pub/Sub")

            # #future = publisher.publish(topic_path, data=str(message_data).encode('utf-8'))
            # # Espera a que se complete la publicación del mensaje
            # #message_id = await future
            # print(f"Mensaje publicado correctamente en Pub/Sub con ID: {message_id}")

            # # await registrarUsuario
            # # print("Mensaje publicado correctamente en Pub/Sub")

            # # Lógica para el resto del comando CreateUser
            # # Por ejemplo, aquí podrías agregar la lógica para crear el usuario en la base de datos
            # # ...
            
            # #response={"Mensaje":"Mensaje publicado correctamente en Pub/Sub"}
            # response={"Msg":"Mensaje creado satisfactoriamente en PUB/SUB", "createdAt":datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            # return response
        

            # Publica el mensaje en el tema de Pub/Sub
            print(f"Vamos a publicar....")

            future = publisher.publish(topic_path, data=str(message_data).encode('utf-8'))
            print(f"se creo el publish.....")
            #message_id = await future
            #message_id = await asyncio.wrap_future(future)

            print(f"Mensaje publicado correctamente en Pub/Sub")

            # Preparar la respuesta
            response = {
                "Msg": "Mensaje creado satisfactoriamente en PUB/SUB",
                "createdAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            return response
        
        except Exception as e:
            print(f"Error al publicar mensaje en Pub/Sub: {e}")
            # Maneja el error adecuadamente, por ejemplo, lanzando una excepción
            raise Exception("Error al publicar mensaje en Pub/Sub")
