from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.')
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    search = StringField('Search Topic')
    submit = SubmitField('search')




