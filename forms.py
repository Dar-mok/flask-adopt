"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL


class PetForm(FlaskForm):
    """Create a from for accepting pets using wtforms"""

    name = StringField("Pet name", validators=[Length(50)])
    species = SelectField('Species',
                          choices=[('cat', 'Cat'), ('dog', 'Dog'),
                                   ('porcupine', 'Porcupine')]
                          )

    photo_url = StringField("Enter photo URL", validators=[Optional(), URL(), Length(150)])

    age = SelectField('Age',
                      choices=[('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'), ('senior', 'Senior')])

    notes = StringField("Additional info")


class EditPet(FlaskForm):
    """form for editing pets"""
    photo_url = StringField("Enter photo URL", validators=[Optional(), URL()])
    notes = StringField("Additional info")
    available = BooleanField("Is available")
