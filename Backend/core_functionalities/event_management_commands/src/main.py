from flask import Flask
from .extensions import db, migrate

from .api.event import event_blueprint
import os
from .config import DevelopmentConfig, ProductionConfig, TestingConfig

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

    migrate.init_app(app, db)
    with app.app_context():
        try:
            db.create_all()
            print("Database tables created or already exist.")
        except Exception as e:
            print(f"Error initializing database tables: {e}")

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
    app.run(host="0.0.0.0", port=3001)