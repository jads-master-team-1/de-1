from database.models import Model, Prediction


class NotFoundError(Exception):
    pass


class ModelRepository:
    def __init__(self, session):
        self._session = session

    def current_model(self):
        model = self._session.query(Model).order_by(Model.id.desc()).first()
        if not model:
            raise NotFoundError()

        return model

    def store_model(self, model):
        self._session.add(model)
        self._session.commit()

        return model


class PredictionRepository:
    def __init__(self, session):
        self._session = session

    def list_predictions(self):
        return self._session.query(Prediction)

    def store_prediction(self, prediction):
        self._session.add(prediction)
        self._session.commit()

        return prediction
