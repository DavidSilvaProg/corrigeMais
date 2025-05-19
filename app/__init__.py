from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.secret_key = os.getenv("CHAVE_SESSION")

    from app.routes.principal_routes import bp_tarefa

    app.register_blueprint(bp_tarefa)

    return app