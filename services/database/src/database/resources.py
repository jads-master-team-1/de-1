import flask

from flask import Blueprint, jsonify

from database.repositories import NotFoundError
from database.interactions import ModelInteractions, PredictionInteractions

resources = Blueprint("api", __name__, url_prefix="/api")


def model_interactions():
    return ModelInteractions(**flask.current_app.repositories)


def prediction_interactions():
    return PredictionInteractions(**flask.current_app.repositories)


@resources.route("/models/", methods=["GET"])
def current_model():
    try:
        return model_interactions().current()
    except NotFoundError:
        return {"message": "No model found"}, 404


@resources.route("/models/", methods=["POST"])
def store_model():
    return model_interactions().store(flask.request.json)


@resources.route("/predictions/", methods=["GET"])
def list_predictions():
    return jsonify(prediction_interactions().list())


@resources.route("/predictions/", methods=["POST"])
def store_prediction():
    return prediction_interactions().store(flask.request.json)
