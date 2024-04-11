import pika

# Conexión al servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaración de una cola
channel.queue_declare(queue='prueba')

# Envío de un mensaje a la cola
channel.basic_publish(exchange='', routing_key='prueba', body='¡Hola, RabbitMQ!')

print(" [x] Mensaje enviado")

# Función para manejar mensajes recibidos
def callback(ch, method, properties, body):
    print(" [x] Mensaje recibido:", body)

# Consumir mensajes de la cola
channel.basic_consume(queue='prueba', on_message_callback=callback, auto_ack=True)

print(' [*] Esperando mensajes. Presiona CTRL+C para salir.')
channel.start_consuming()