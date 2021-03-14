from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import InputRequired, Email, Optional, Length

species_list =["cat", "dog", "fish", "porcupine"]

class AddPetForm(FlaskForm):
    """Model for pet add form"""
    pet_name = StringField("Pet name", validators=[InputRequired(message="Name cannot be blank")])
    species = SelectField("Pet species", validators=[InputRequired(message="Species cannot be blank")], choices=[(spc, spc) for spc in species_list])
    photo_url = URLField("Pet photo", validators=[Optional()])
    age = IntegerField("Pet age", validators=[Optional(), Length(min=0, max=30)])
    note = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Model for pet edit form"""
    photo_url = URLField("Pet photo", validators=[Optional()])
    note = StringField("Notes", validators=[Optional()])
    available = BooleanField("This pet is available")