# main.py

from flask import Flask
from extensions import db
from flask import Flask
from flask_cors import CORS

from api.training_plan import training_plan_blueprint
from models.training_plan import TrainingPlan  # Importa tus modelos aquí


# Configuration
DATABASE_URI = 'sqlite:///C:/Users/angey/OneDrive/Escritorio/ProyectoFinal/MISW4501-Proyecto-final-Grupo-9/Backend/training_management/src/trainingmanagement.db'

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    # Initialize app with SQLAlchemy
    db.init_app(app)

    # Reg
    # Register blueprints
    app.register_blueprint(training_plan_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        print("dame tiempo!!!")
        db.create_all()  # Create database tables for our data models
    app.run(debug=True)