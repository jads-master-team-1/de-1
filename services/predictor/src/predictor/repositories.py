import pickle

from predictor.client import WebClientError


class ModelNotAvailableError(Exception):
    pass


class PredictorRepository:
    def __init__(self, database_client, storage_client):
        self._database_client = database_client
        self._storage_client = storage_client

        try:
            self.load_model()
        except WebClientError:
            pass

    def load_model(self):
        model = self._database_client.get("/models/")
        name = model["file"]

        file = self._storage_client.get(f"/files/{name}", raw=True)

        self._model = pickle.loads(file)

    def create_prediction(self, inputs):
        if not hasattr(self, "_model") or not self._model:
            raise ModelNotAvailableError()

        return self._model.predict([inputs])[0]
