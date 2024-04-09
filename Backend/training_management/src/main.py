import os
from flask import Flask
from .extensions import db
from src.config import DevelopmentConfig, TestingConfig, ProductionConfig
from .api.training_plan import training_plan_blueprint

# Configuration
DATABASE_URI = 'sqlite:///trainingmanagement.db'

def create_app(config_object=None):
    app = Flask(__name__)

    # Explicitly set configuration based on the input parameter
    if config_object:
        app.config.from_object(config_object)
    else:
        # Default to DevelopmentConfig if nothing is specified
        app.config.from_object(DevelopmentConfig)
    #app.config.from_object(config_object)
    #config_type = os.getenv('FLASK_ENVIRONMENT', 'DevelopmentConfig')
    #if config_type == 'TestingConfig':
    #    app.config.from_object(TestingConfig)
    #elif config_type == 'ProductionConfig':
    #    app.config.from_object(ProductionConfig)
    #else:
    #    app.config.from_object(DevelopmentConfig)
    # Database configuration
    #app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    # Initialize app with SQLAlchemy
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(training_plan_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
       db.create_all()  # Create database tables for our data models
    app.run(debug=True)