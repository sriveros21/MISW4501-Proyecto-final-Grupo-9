from flask import Flask
from extensions import db
from api.training_plan import training_plan_blueprint

# Configuration
DATABASE_URI = 'sqlite:///trainingmanagement.db'

def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

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