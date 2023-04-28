"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, Optional, Email, URL

class Pet(FlaskForm):
    """Create a from for accepting pets using wtforms"""

    name = StringField("Pet name")
    species = StringField("Enter species")
    photo_url = StringField("Enter photo URL", validators=[URL()])
    age = FloatField("Enter Age")
    notes = StringField("Additional info")

