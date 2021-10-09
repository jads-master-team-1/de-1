import os

from flask import Flask
from werkzeug.exceptions import HTTPException

from predictor.repositories import PredictorRepository
from predictor.resources import resources
from predictor.client import WebClient


def create_app():
    # Create app
    app = Flask(__name__)

    # Register resources
    app.register_blueprint(resources)

    # Register health
    @app.route("/api/health/")
    def default_health():
        return {"status": "OK"}

    # Register errors
    @app.errorhandler(HTTPException)
    def default_handler(error):
        return {"message": error.name}, error.code

    # Create clients
    database_endpoint = os.getenv("FLASK_DATABASE_SERVICE")
    storage_endpoint = os.getenv("FLASK_STORAGE_SERVICE")

    database_client = WebClient(database_endpoint)
    storage_client = WebClient(storage_endpoint)

    # Create repositories
    setattr(
        app,
        "repositories",
        {
            "predictor_repository": PredictorRepository(
                database_client,
                storage_client,
            ),
        },
    )

    return app
