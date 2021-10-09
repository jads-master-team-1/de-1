import flask

from flask import Blueprint, Response, jsonify

from web.client import WebClientError
from web.interactions import (
    ModelInteractions,
    PredictionInteractions,
    VisualizationInteractions,
)


resources = Blueprint("api", __name__, url_prefix="/api")


def model_interactions():
    return ModelInteractions(**flask.current_app.repositories)


def prediction_interactions():
    return PredictionInteractions(**flask.current_app.repositories)


def visualization_interactions():
    return VisualizationInteractions(**flask.current_app.repositories)


@resources.route("/models/", methods=["POST"])
def store_model():
    try:
        if not flask.request.content_type.startswith("multipart/form-data"):
            return {"message": "Invalid content type"}, 400

        if not flask.request.files.get("file"):
            return {"message": "Invalid model file"}, 400

        return model_interactions().store(flask.request.files.get("file"))
    except WebClientError:
        return {"message": "An error occurred in an internal service"}, 500


@resources.route("/predictions/", methods=["GET"])
def get_predictions():
    try:
        return jsonify(prediction_interactions().list())
    except WebClientError:
        return {"message": "An error occurred in an internal service"}, 500


@resources.route("/predictions/", methods=["POST"])
def create_prediction():
    try:
        return prediction_interactions().create(flask.request.json)
    except WebClientError:
        return {"message": "An error occurred in an internal service"}, 500


@resources.route("/visualization/", methods=["GET"])
def create_visualization():
    try:
        return Response(
            visualization_interactions().create(),
            mimetype="image/png",
        )
    except WebClientError:
        return {"message": "An error occurred in an internal service"}, 500
