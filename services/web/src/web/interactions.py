class ModelInteractions:
    def __init__(self, **repositories):
        self._database_repository = repositories["database_repository"]
        self._predictor_repository = repositories["predictor_repository"]
        self._storage_repository = repositories["storage_repository"]

    def store(self, file):
        file = self._storage_repository.store_file(file)
        model = self._database_repository.store_model(file["name"])

        self._predictor_repository.load_model()

        return model


class PredictionInteractions:
    def __init__(self, **repositories):
        self._database_repository = repositories["database_repository"]
        self._predictor_repository = repositories["predictor_repository"]

    def list(self):
        return self._database_repository.list_predictions()

    def create(self, data):
        prediction = self._predictor_repository.create_prediction(data)

        return self._database_repository.store_prediction(
            {
                "input": data,
                "output": prediction["output"],
            }
        )


class VisualizationInteractions:
    def __init__(self, **repositories):
        self._database_repository = repositories["database_repository"]
        self._visualization_repository = repositories["visualization_repository"]

    def create(self):
        predictions = self._database_repository.list_predictions()

        return self._visualization_repository.create_visualization(predictions)
