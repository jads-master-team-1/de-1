import os

from flask import Flask
from werkzeug.exceptions import HTTPException

from database.repositories import ModelRepository, PredictionRepository
from database.resources import resources
from database.db import db


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

    # Create database
    host = os.getenv("FLASK_DB_HOST")
    port = os.getenv("FLASK_DB_PORT")
    user = os.getenv("FLASK_DB_USER")
    password = os.getenv("FLASK_DB_PASSWORD")
    name = os.getenv("FLASK_DB_NAME")

    uri = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"
    app.config["SQLALCHEMY_DATABASE_URI"] = uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    db.create_all(app=app)

    # Create repositories
    setattr(
        app,
        "repositories",
        {
            "model_repository": ModelRepository(db.session),
            "prediction_repository": PredictionRepository(db.session),
        },
    )

    return app
