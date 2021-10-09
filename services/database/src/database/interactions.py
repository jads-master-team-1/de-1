from database.models import Model, Prediction


class ModelInteractions:
    def __init__(self, **repositories):
        self._model_repository = repositories["model_repository"]

    def current(self):
        return self._model_repository.current_model().to_dict()

    def store(self, data):
        model = Model(file=data["file"])

        return self._model_repository.store_model(model).to_dict()


class PredictionInteractions:
    def __init__(self, **repositories):
        self._prediction_repository = repositories["prediction_repository"]

    def list(self):
        return [p.to_dict() for p in self._prediction_repository.list_predictions()]

    def store(self, data):
        prediction = Prediction(input=data["input"], output=data["output"])

        return self._prediction_repository.store_prediction(prediction).to_dict()
