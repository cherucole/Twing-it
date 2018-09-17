from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.')
    submit = SubmitField('Submit')