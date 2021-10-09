class VisualizationInteractions:
    def __init__(self, **repositories):
        self._visualization_repository = repositories["visualization_repository"]

    def create(self, data):
        return self._visualization_repository.create_prediction_visualization(data)
