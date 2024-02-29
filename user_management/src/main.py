from dotenv import load_dotenv
from flask import Flask, jsonify
from .blueprints.users import users_blueprint
from .errors.errors import ApiError
import os
#from .models.database import init_db
from .models.database import init_db

loaded = load_dotenv('.env.development')


app = Flask(__name__)
app.register_blueprint(users_blueprint)
init_db()

@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
      "mssg": err.description,
      "version": os.environ["VERSION"]
    }
    return jsonify(response), err.code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3005)