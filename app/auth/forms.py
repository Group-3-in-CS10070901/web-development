from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField,FileField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

class Detailed_informationForm(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired(), Length(1, 64)])
    main_image = FileField('main_image', validators=[DataRequired()])
    gender=SelectField('gender：', choices=[
        ('male', '男'),
        ('female', '女'),
        ('unknown', '保密')
    ])
    love_state=SelectField('love_state：', choices=[
        ('single', '单身'),
        ('divorce', '离婚'),
        ('unknown', '保密')
    ])
    sexuality=SelectField('sexuality：', choices=[
        ('male', '男'),
        ('female', '女'),
        ('double','双性恋'),
        ('unknown', '保密')
    ])
    height = StringField('height', validators=[DataRequired(), Length(1, 64)])
    salary=StringField('salary', validators=[Length(1, 64)])
    about_me = StringField('about_me', validators=[Length(1, 64)])
    contact_information = StringField('contact_information', validators=[DataRequired(), Length(1, 64)])
    #出生日期
    #所在地
    submit = SubmitField('submit')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    password = PasswordField('New password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm new password',
                              validators=[DataRequired()])
    submit = SubmitField('Update Password')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    password = PasswordField('New Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')

    
    
    
