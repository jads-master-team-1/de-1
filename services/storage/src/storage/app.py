import os

from flask import Flask
from werkzeug.exceptions import HTTPException

from storage.repositories import StorageRepository
from storage.resources import resources


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

    # Get files path
    base_path = os.getenv("FLASK_FILES_PATH")

    # Create repositories
    setattr(
        app,
        "repositories",
        {
            "storage_repository": StorageRepository(base_path),
        },
    )

    return app
