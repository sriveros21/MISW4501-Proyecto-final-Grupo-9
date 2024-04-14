import json, os
from google.cloud import pubsub_v1

def publish_to_pubsub(request):
    if request.method != 'POST' or not request.get_json():
        return 'Petición no válida', 400

    # Obtiene los datos JSON de la petición
    request_data = request.get_json()

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "proyecto-final-miso-416801-9cf3fcab0edf.json"

    # Nombre del tema de Pub/Sub al que quieres publicar
    topic_name = 'registrar-usuario'

    # Crea un cliente de Pub/Sub
    publisher = pubsub_v1.PublisherClient()

    # Formatea el nombre del tema
    topic_path = publisher.topic_path('proyecto-final-miso-416801', topic_name)

    # Convierte la petición a JSON
    message_data = json.dumps(request_data).encode('utf-8')

    # Publica el mensaje en el tema
    future = publisher.publish(topic_path, data=message_data)
    
    # Espera a que se complete la publicación
    future.result()

    return 'Se ha creado una solicitud para creación del usuario', 200