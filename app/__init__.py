from flask import Flask
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv

mongo = PyMongo()
load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
    
    mongo.init_app(app)

    # Register Blueprints here
    from app.routes.movies import movies_bp
    app.register_blueprint(movies_bp)

    return app