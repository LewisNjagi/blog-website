from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required
from wtforms.validators import Email
from ..models import Subscriber
from wtforms import ValidationError


class BlogForm(FlaskForm):

    title = StringField('Blog title',validators=[Required()])
    blog = TextAreaField('Add a Blog', validators=[Required()]) 
    category = SelectField('Choose Blog Category', choices = [('Travel','Travel'),('Music','Music'),('Photography','Photography'),('Food','Food')],validators=[Required()])
    submit = SubmitField('Add')

class CommentForm(FlaskForm):

    comment = TextAreaField('Add a comment', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    submit = SubmitField('Submit')

    def validate_email(self,data_field):
        if Subscriber.query.filter_by(email = data_field.data).first():
            raise ValidationError('You are already subscribed')