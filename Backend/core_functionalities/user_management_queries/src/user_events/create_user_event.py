from ..commands.create_user_command import CreateUser
from google.cloud import pubsub_v1
import json

def callback(message):
    print(f"Mensaje recibido: {message}")
    data = message.data.decode("utf-8")  # Decodifica los datos del mensaje
    result = create_user_from_pubsub_message(data)
    print(f"Resultado de crear usuario: {result}")
    message.ack()


def subscribe_to_pubsub(project_id, subscription_name, credentials_path):
    subscriber = pubsub_v1.SubscriberClient.from_service_account_json(credentials_path)

    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Esperando mensajes en la suscripción: {subscription_path}")

    try:
        streaming_pull_future.result()
    except Exception as e:
        streaming_pull_future.cancel()
        print(f"Error: {e}")

def create_user_from_pubsub_message(data):
    fields_request = ['username', 'password', 'email', 'dni', 'fullName', 'phoneNumber']
    data_dict = json.loads(data) 
    
    for field in fields_request:
        if field not in data_dict:
            data_dict[field] = ""
    
    result = CreateUser(data_dict['username'], data_dict['password'], data_dict['email'], data_dict['dni'], data_dict['fullName'], data_dict['phoneNumber']).execute()

    return result


