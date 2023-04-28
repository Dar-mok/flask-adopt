"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, Email, URL


class PetForm(FlaskForm):
    """Create a from for accepting pets using wtforms"""

    name = StringField("Pet name")
    species = SelectField('Species',
    choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')]
)
    #cat, dog, porcupine

    photo_url = StringField("Enter photo URL", validators=[Optional(), URL()])

    age = SelectField('Age',
    choices=[('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'),('senior', 'Senior')])

    notes = StringField("Additional info")
