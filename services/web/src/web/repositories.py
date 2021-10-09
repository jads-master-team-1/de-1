class DatabaseRepository:
    def __init__(self, client):
        self._client = client

    def store_model(self, name):
        return self._client.post("/models/", data={"file": name})

    def store_prediction(self, prediction):
        return self._client.post("/predictions/", data=prediction)

    def list_predictions(self):
        return self._client.get("/predictions/")


class PredictorRepository:
    def __init__(self, client):
        self._client = client

    def load_model(self):
        self._client.put("/models/", raw=True)

    def create_prediction(self, inputs):
        return self._client.post("/predictions/", data=inputs)


class StorageRepository:
    def __init__(self, client):
        self._client = client

    def store_file(self, file):
        return self._client.post("/files/", file=file)


class VisualizationRepository:
    def __init__(self, client):
        self._client = client

    def create_visualization(self, predictions):
        return self._client.post("/visualization/", data=predictions, raw=True)
