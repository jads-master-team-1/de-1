import os
import io
import hashlib


class StorageRepository:
    def __init__(self, base_path):
        self._base_path = base_path

        self._ensure_exists(base_path)

    def load_file(self, name):
        with open(self._base_path + name, "rb") as handle:
            return io.BytesIO(handle.read())

    def store_file(self, file):
        content = file.read()
        digest = hashlib.md5(content).hexdigest()
        extension = file.filename.split(".")[-1]

        name = f"{digest}.{extension}"

        with open(self._base_path + name, "wb") as handle:
            handle.write(content)

        return name

    def _ensure_exists(self, path):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError:
            pass
