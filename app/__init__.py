from flask import Flask
import os
from dotenv import load_dotenv


load_dotenv()

def create_app():
    app = Flask(__name__)


    # Register Blueprints here
    # from app.routes.movies import movies_bp
    # app.register_blueprint(movies_bp)

    return app