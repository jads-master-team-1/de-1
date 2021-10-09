from sqlalchemy_utils import ScalarListType

from database.db import db


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    file = db.Column(db.String, nullable=False)
    created_on = db.Column(
        db.DateTime,
        server_default=db.func.now(),
    )
    updated_on = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        server_onupdate=db.func.now(),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "file": self.file,
            "created_on": self.created_on.isoformat(),
            "updated_on": self.updated_on.isoformat(),
        }


class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    input = db.Column(ScalarListType(float), nullable=False)
    output = db.Column(db.Integer, nullable=False)
    created_on = db.Column(
        db.DateTime,
        server_default=db.func.now(),
    )
    updated_on = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        server_onupdate=db.func.now(),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "input": self.input,
            "output": self.output,
            "created_on": self.created_on.isoformat(),
            "updated_on": self.updated_on.isoformat(),
        }
