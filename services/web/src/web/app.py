import os

from flask import Flask
from werkzeug.exceptions import HTTPException

from web.repositories import (
    DatabaseRepository,
    PredictorRepository,
    StorageRepository,
    VisualizationRepository,
)
from web.resources import resources
from web.client import WebClient


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
    predictor_endpoint = os.getenv("FLASK_PREDICTOR_SERVICE")
    storage_endpoint = os.getenv("FLASK_STORAGE_SERVICE")
    visualization_endpoint = os.getenv("FLASK_VISUALIZATION_SERVICE")

    database_client = WebClient(database_endpoint)
    predictor_client = WebClient(predictor_endpoint)
    storage_client = WebClient(storage_endpoint)
    visualization_client = WebClient(visualization_endpoint)

    # Create repositories
    setattr(
        app,
        "repositories",
        {
            "database_repository": DatabaseRepository(database_client),
            "predictor_repository": PredictorRepository(predictor_client),
            "storage_repository": StorageRepository(storage_client),
            "visualization_repository": VisualizationRepository(visualization_client),
        },
    )

    return app
