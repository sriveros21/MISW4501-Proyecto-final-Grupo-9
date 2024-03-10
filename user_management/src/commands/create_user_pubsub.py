from .base_command import BaseCommand
from ..errors.errors import InvalidParams, EmailUsernameExist
from google.cloud import pubsub_v1  # Importa la biblioteca cliente de Pub/Sub
import asyncio

# Define la clase CreateUser
class CreateUserPubSub(BaseCommand):
    def __init__(self, username, password, email, dni, fullName, phoneNumber):
        self.username = username
        self.password = password
        self.email = email
        self.dni = dni
        self.fullName = fullName
        self.phoneNumber = phoneNumber

    async def execute(self):
        # Crea un cliente de Pub/Sub
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
        registrarUsuario = publisher.publish(topic_path, data=str(message_data).encode('utf-8'))

        try:
            # Espera a que se complete la publicación del mensaje
            await registrarUsuario
            print("Mensaje publicado correctamente en Pub/Sub")

            # Lógica para el resto del comando CreateUser
            # Por ejemplo, aquí podrías agregar la lógica para crear el usuario en la base de datos
            # ...

        except Exception as e:
            print(f"Error al publicar mensaje en Pub/Sub: {e}")
            # Maneja el error adecuadamente, por ejemplo, lanzando una excepción
            raise Exception("Error al publicar mensaje en Pub/Sub")

