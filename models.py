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
        autoincrement = True,
        primary_key=True
    )

    name = db.Column(
        db.String(50),
        nullable = False
    )

    species = db.Column(
        db.String(50),
        nullable = False
    )

    photo_url = db.Column(
        db.String(150),
        nullable = False,
        default = ""
    )

    age = db.Column(
        db.String(20)
        # choices about baby and senoir and such?
    )

    notes = db.Column(
        db.String
    )

    available = db.Column(
        db.Boolean,
        nullable = False,
        default = True
    )