class PredictorInteractions:
    def __init__(self, **repositories):
        self._predictor_repository = repositories["predictor_repository"]

    def load(self):
        self._predictor_repository.load_model()

    def create(self, data):
        prediction = self._predictor_repository.create_prediction(data)

        return {"output": float(prediction)}
