import flask

from flask import Blueprint

from predictor.client import WebClientError
from predictor.repositories import ModelNotAvailableError
from predictor.interactions import PredictorInteractions


resources = Blueprint("api", __name__, url_prefix="/api")


def predictor_interactions():
    return PredictorInteractions(**flask.current_app.repositories)


@resources.route("/models/", methods=["PUT"])
def load_model():
    try:
        predictor_interactions().load()

        return "", 204
    except WebClientError:
        return {"message": "An error occured while loading the model"}, 500


@resources.route("/predictions/", methods=["POST"])
def create_prediction():
    try:
        return predictor_interactions().create(flask.request.json)
    except ValueError:
        return {"message": "Invalid amount of features"}, 400
    except ModelNotAvailableError:
        return {"message": "An error occured while loading the model"}, 500
