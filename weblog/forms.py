from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=3)]
                           )
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(),
                                                     Length(min=3, max=25)])
    confirm_password = PasswordField('confirm password',
                                     validators=[DataRequired(), EqualTo('password')]
                                     )


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    Remember = BooleanField('Remember me')
