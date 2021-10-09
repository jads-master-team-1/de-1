import flask

from flask import Blueprint, Response

from visualization.interactions import VisualizationInteractions


resources = Blueprint("api", __name__, url_prefix="/api")


def visualization_interactions():
    return VisualizationInteractions(**flask.current_app.repositories)


@resources.route("/visualization/", methods=["POST"])
def create_visualization():
    try:
        if len(flask.request.json) == 0:
            return {"message": "Invalid amount of predictions"}, 400

        return Response(
            visualization_interactions().create(flask.request.json),
            mimetype="image/png",
        )
    except TypeError:
        return {"message": "An error occured while plotting the predictions"}, 500
