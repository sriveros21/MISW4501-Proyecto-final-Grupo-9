from flask import Flask, jsonify
from .extensions import db, migrate
from .api.training_plan import training_api, training_plan_blueprint
from .api.training_sesion import training_session_blueprint
from .config import DevelopmentConfig, ProductionConfig, TestingConfig
from .queries.listen_training import start_listener_in_background
from .queries.listen_metrics import start_listener_in_background as start_listener_in_background_metrics
from .queries.listen_plan import start_listener_in_background as start_listener_in_background_plan
from .models.training_session import TrainingSession
import os

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'production':
        app.config.from_object(ProductionConfig)
    elif env == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    print("Environment:", env)
    print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(training_api)
    app.register_blueprint(training_plan_blueprint)
    app.register_blueprint(training_session_blueprint)
    from .models.training_session import TrainingSession
    start_listener_in_background(app)
    start_listener_in_background_metrics(app)
    start_listener_in_background_plan(app)
    # # Optional: Add a CLI command to insert default data
    # @app.cli.command('insert-data')
    # def insert_default_data():
    #     insert_data_function()  # Define this function to insert data

    return app

# app = Flask(__name__)
# app.register_blueprint(training_api)
# app.register_blueprint(training_plan_blueprint)



# Este método debe eliminarse, cuando la aplicación esé completa, para el desarrollo de la HU011
# se deja para pruebas.
# def insert_data_function():
#     default_training_data = [
#         {
#             'date': '2024-04-06',
#             'username': 'usuario1',
#             'sport': 'running',
#             'time': '1 hour',
#             'distance': '5 km',
#             'weight': '70 kg',
#             'intensity': 'medium',
#             'series': '3',
#             'calories': '300 kcal'
#         },
#         {
#             'date': '2024-04-03',
#             'username': 'usuario1',
#             'sport': 'running',
#             'time': '1 hour',
#             'distance': '5 km',
#             'weight': '70 kg',
#             'intensity': 'medium',
#             'series': '3',
#             'calories': '300 kcal'
#         },
#         {
#             'date': '2024-04-04',
#             'username': 'usuario1',
#             'sport': 'running',
#             'time': '1 hour',
#             'distance': '5 km',
#             'weight': '70 kg',
#             'intensity': 'medium',
#             'series': '3',
#             'calories': '300 kcal'
#         },
#     ]

#     for data in default_training_data:
#         training = TrainingHistory(
#             date=data['date'],
#             username=data['username'],
#             sport=data['sport'],
#             time=data['time'],
#             distance=data['distance'],
#             weight=data['weight'],
#             intensity=data['intensity'],
#             series=data['series'],
#             calories=data['calories']
#         )
#         db.add(training)
    
#     # Commit para guardar los cambios en la base de datos
#     db.commit()

if __name__ == '__main__':
    
    app = create_app()
    # project_id = 'proyecto-final-miso-416801'
    # subscription_name = 'evento-registrar-usuario'
    # credentials_path = 'proyecto-final-miso-416801-9cf3fcab0edf.json'
    # subscribe_to_pubsub(project_id, subscription_name, credentials_path)

    app.run(host="0.0.0.0", port=3003)
