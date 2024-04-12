from flask import Flask
from .extensions import db, migrate
from .config import DevelopmentConfig, TestingConfig, ProductionConfig
from .api.training_plan import training_plan_blueprint
from .api.training_session import training_session_blueprint
from .api.training_metrics import training_metrics_blueprint
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
    
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(training_plan_blueprint)
    app.register_blueprint(training_session_blueprint)
    app.register_blueprint(training_metrics_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=3004)