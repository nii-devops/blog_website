
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired, URL, EqualTo, Length
from flask_ckeditor import CKEditorField


categories = categories = [
        "Art & Culture",
        "DIY & Crafts",
        "Education",
        "Entertainment",
        "Environment & Sustainability",
        "Fashion & Beauty",
        "Finance & Business",
        "Food & Recipes",
        "Health & Wellness",
        "Home & Garden",
        "Lifestyle",
        "News & Politics",
        "Parenting & Family",
        "Personal Development",
        "Pets & Animals",
        "Relationships & Dating",
        "Science & Innovation",
        "Sports & Fitness",
        "Technology",
        "Travel",
        "Others"
        ]

# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    category    = SelectField("Blog Post Category", choices=categories, validators=[DataRequired()])
    title       = StringField("Blog Post Title", validators=[DataRequired()])
    #subtitle    = StringField("Subtitle", validators=[DataRequired()])
    img_url     = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body        = CKEditorField("Blog Content", validators=[DataRequired()])
    submit      = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    f_name      = StringField(label='First name(s)', validators=[DataRequired()])
    l_name      = StringField(label='Last name', validators=[DataRequired()])
    email       = EmailField(label='Email', validators=[DataRequired()])
    password    = PasswordField(label='Password', validators=[Length(min=8), DataRequired(), EqualTo('password_2', message='Passwords must match')])
    password_2  = PasswordField(label='Repeat Password', validators=[DataRequired()] )
    submit      = SubmitField("Register")


class LoginForm(FlaskForm):
    email       = EmailField(label='Email', validators=[DataRequired()])
    password    = PasswordField(label='Password', validators=[DataRequired()])
    submit      = SubmitField("Login")


class CommentForm(FlaskForm):
    text    = CKEditorField("Add a Comment", validators=[DataRequired()])
    submit  = SubmitField("Submit Comment")

