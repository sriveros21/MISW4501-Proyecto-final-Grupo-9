from flask import Flask
from api.training_plan import training_plan_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(training_plan_blueprint)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)























# from dotenv import load_dotenv
# from flask import Flask, jsonify
# # from .user_events.users import api_users
# from .user_events.create_user_event import subscribe_to_pubsub
# from .errors.errors import ApiError
# import os
# from .models.database import init_db


# loaded = load_dotenv('.env.development')


# app = Flask(__name__)
# # app.register_blueprint(api_users)
# init_db()

# @app.errorhandler(ApiError)
# def handle_exception(err):
#     response = {
#       "mssg": err.description,
#       "version": os.environ["VERSION"]
#     }
#     return jsonify(response), err.code


# if __name__ == '__main__':
#     project_id = 'proyecto-final-miso-416801'
#     subscription_name = 'evento-registrar-usuario'
#     credentials_path = 'proyecto-final-miso-416801-9cf3fcab0edf.json'
#     subscribe_to_pubsub(project_id, subscription_name, credentials_path)

#     app.run(host="0.0.0.0", port=3000)
