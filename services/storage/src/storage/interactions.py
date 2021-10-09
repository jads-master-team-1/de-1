class StorageInteractions:
    def __init__(self, **repositories):
        self._storage_repository = repositories["storage_repository"]

    def load(self, name):
        return self._storage_repository.load_file(name)

    def store(self, file):
        name = self._storage_repository.store_file(file)

        return {"name": name}
