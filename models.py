"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """"create instances of Pet"""

    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        autoincrementing = True
    )

    name = db.Column(
        type = VARCHAR(50),
        nullable = False
    )

    species = db.Column(
        type = VARCHAR(50),
        nullable = False
    )

    photo_url = db.Column(
        type = VARCHAR(150),
        nullable = False,
        default = ""
    )

    age = db.Column(
        type = VARCHAR(3)
        # choices about baby and senoir and such?
    )

    notes = db.Column(
        type = TEXT
    )

    available = db.Column(
        type = BOOLEAN,
        nullable = False,
        default = True
    )