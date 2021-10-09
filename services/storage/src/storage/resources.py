import flask

from flask import Blueprint, Response

from storage.interactions import StorageInteractions


resources = Blueprint("api", __name__, url_prefix="/api")


def storage_interactions():
    return StorageInteractions(**flask.current_app.repositories)


@resources.route("/files/<name>", methods=["GET"])
def load_file(name):
    try:
        return Response(
            storage_interactions().load(name),
            mimetype="application/octet-stream",
        )
    except OSError:
        return {"message": "An error occured while loading the file"}, 404


@resources.route("/files/", methods=["POST"])
def store_file():
    try:
        if not flask.request.content_type.startswith("multipart/form-data"):
            return {"message": "Invalid content type"}, 400

        if not flask.request.files.get("file"):
            return {"message": "Invalid file"}, 400

        return storage_interactions().store(flask.request.files.get("file"))
    except OSError:
        return {"message": "An error occured while storing the file"}, 500
