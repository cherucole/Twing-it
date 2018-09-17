# from flask_wtf import FlaskForm
# from wtforms import StringField,TextAreaField,SubmitField, SelectField
#
# class BlogpostForm(FlaskForm):
#
#     title = StringField('Blogpost title')
#     category_id = SelectField('Blogpost Category', choices=[('thoughts', 'thoughts'),
#                                                       ('technical', 'technical'),
#                                                       ('comedy', 'comedy'),
#                                                       ('politics', 'politics')])
#     content = TextAreaField('Post Of The Blogpost')
#     submit = SubmitField('Submit')
#
#
# class CommentForm(FlaskForm):
#
#     title = StringField('Comment Title')
#     comment = TextAreaField('Post Of The Comment')
#     submit = SubmitField('Submit')
#
#
# class CategoryForm(FlaskForm):
#
#     title = StringField('Blogpost title')
#     Blogpost = TextAreaField('Post Of The Comment')
#     submit = SubmitField('Submit')
#
#
# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Tell us about you.')
#     submit = SubmitField('Submit')