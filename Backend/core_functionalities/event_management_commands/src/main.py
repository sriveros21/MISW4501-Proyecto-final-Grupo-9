from flask import Flask
from .extensions import db
#from flask_migrate import Migrate
from .api.event import event_blueprint
import os
from .config import DevelopmentConfig, ProductionConfig, TestingConfig

# Configuration
#DATABASE_URI = os.environ.get("DATABASE_URL")
#migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Select configuration based on FLASK_ENV environment variable
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'production':
        app.config.from_object(ProductionConfig)
    elif env == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    #migrate.init_app(app, db)
    print(f"Database URL: {app.config['SQLALCHEMY_DATABASE_URI']}")
    with app.app_context():
        try:
            db.create_all()
            print("Database tables created or already exist.")
        except Exception as e:
            print(f"Error initializing database tables: {e}")

    #    from .api.event import event_blueprint  # Import models here to ensure they are registered
    #    db.create_all()
    # Register blueprints
    app.register_blueprint(event_blueprint)

    # Function to register CLI commands
    # def register_cli_commands(app):
    #     @app.cli.command("init-db")
    #     def init_db():
    #         """Create database tables."""
    #         db.create_all()
    #         print("Database tables created.")
    
    # register_cli_commands(app)

    return app

if __name__ == "__main__":
    app = create_app()
    # with app.app_context():
    #     db.create_all()  # Create database tables for our data models
    app.run(host="0.0.0.0", port=3001)