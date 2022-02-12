from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, HiddenField, FileField,IntegerField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField
from HS3.models import Survey
from HS3 import db

def Sites():
    return db.session.query(Survey).all()

class SubmitForm(FlaskForm):
    site = QuerySelectField("Site", query_factory= Sites , allow_blank=False, get_label='name')
    email = StringField(label="Email:", validators=[Email(), DataRequired()])
    video = FileField('Video:', validators=[DataRequired()])
    submit = SubmitField(label='Upload video')

class SiteForm(FlaskForm):
    name = StringField(label='Name:')
    site = StringField(label='Site:')
    date = StringField(label='Date:')
    road = StringField(label='Road:')
    town = StringField(label='Town:')
    county = StringField(label='County:')
    phone = StringField(label='Phone Number:')
    email = StringField(label='Email:', validators=[Email()])
    pipe_use = StringField(label='Pipe use:')
    year_laid = StringField(label='Year Laid:')
    pipe_length = StringField(label='Pipe Length:')
    pipe_shape = StringField(label='Pipe Shape:')
    pipe_size = StringField(label='Pipe Size:')
    pipe_material = StringField(label='Pipe Material:')
    submit = SubmitField(label='Add Site Data')

class EditForm(FlaskForm):
    site_select = QuerySelectField("Site", query_factory=Sites, allow_blank=False, get_label ='name')
    name = StringField(label='Name:')
    site = StringField(label='Site:')
    date = StringField(label='Date:')
    road = StringField(label='Road:')
    town = StringField(label='Town:')
    county = StringField(label='County:')
    phone = StringField(label='Phone Number:')
    email = StringField(label='Email:', validators=[Email()])
    pipe_use = StringField(label='Pipe use:')
    year_laid = StringField(label='Year Laid:')
    pipe_length = StringField(label='Pipe Length:')
    pipe_shape = StringField(label='Pipe Shape:')
    pipe_size = StringField(label='Pipe Size:')
    pipe_material = StringField(label='Pipe Material:')
    submit_update = SubmitField(label='Update Site')
    submit_delete = SubmitField(label='Delete Site')
    submit_commit = SubmitField(label="Commit Update")