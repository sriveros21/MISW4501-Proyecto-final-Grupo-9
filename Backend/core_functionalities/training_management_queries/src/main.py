from dotenv import load_dotenv
from flask import Flask, jsonify
from .api.training_api import training_api, training_plan_blueprint
# from .user_events.create_user_event import subscribe_to_pubsub
# from .errors.errors import ApiError
# import os
from .models.database_queries import init_db_queries, db_session_queries
from .models.training_history import TrainingHistory


loaded = load_dotenv('.env.development')


app = Flask(__name__)
app.register_blueprint(training_api)
app.register_blueprint(training_plan_blueprint)
init_db_queries()



# Este método debe eliminarse, cuando la aplicación esé completa, para el desarrollo de la HU011
# se deja para pruebas.
def insert_default_data():
    default_training_data = [
        {
            'date': '2024-04-06',
            'username': 'usuario1',
            'sport': 'running',
            'time': '1 hour',
            'distance': '5 km',
            'weight': '70 kg',
            'intensity': 'medium',
            'series': '3',
            'calories': '300 kcal'
        },
        {
            'date': '2024-04-03',
            'username': 'usuario1',
            'sport': 'running',
            'time': '1 hour',
            'distance': '5 km',
            'weight': '70 kg',
            'intensity': 'medium',
            'series': '3',
            'calories': '300 kcal'
        },
        {
            'date': '2024-04-04',
            'username': 'usuario1',
            'sport': 'running',
            'time': '1 hour',
            'distance': '5 km',
            'weight': '70 kg',
            'intensity': 'medium',
            'series': '3',
            'calories': '300 kcal'
        },
    ]

    for data in default_training_data:
        training = TrainingHistory(
            date=data['date'],
            username=data['username'],
            sport=data['sport'],
            time=data['time'],
            distance=data['distance'],
            weight=data['weight'],
            intensity=data['intensity'],
            series=data['series'],
            calories=data['calories']
        )
        db_session_queries.add(training)
    
    # Commit para guardar los cambios en la base de datos
    db_session_queries.commit()

insert_default_data()


# @app.errorhandler(ApiError)
# def handle_exception(err):
#     response = {
#       "mssg": err.description,
#       "version": os.environ["VERSION"]
#     }
#     return jsonify(response), err.code


if __name__ == '__main__':
    
    print("Esto entra aquí")
    insert_default_data()
    # project_id = 'proyecto-final-miso-416801'
    # subscription_name = 'evento-registrar-usuario'
    # credentials_path = 'proyecto-final-miso-416801-9cf3fcab0edf.json'
    # subscribe_to_pubsub(project_id, subscription_name, credentials_path)

    app.run(host="0.0.0.0", port=3000)
