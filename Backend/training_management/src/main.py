from flask import Flask
from api.training_plan import training_plan_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(training_plan_blueprint)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)