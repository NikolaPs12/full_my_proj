from wtforms import StringField, PasswordField, validators, FileField, SubmitField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileAllowed
from .models.user import User
from .models.post import Post

class RegisterForm(FlaskForm):
    username = StringField('ФИО', validators=[DataRequired(), Length(min=2, max=150 ) ]) 
    email = StringField('емаил', validators=[DataRequired(), Email()])
    password = PasswordField('пароль', validators=[DataRequired(), Length(min=6, max=100)])
    confirm_password = PasswordField('повторите пароль', validators=[DataRequired(), Length(min=6, max=100), EqualTo('password')])
    avatar = FileField('аватарка', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Регистрация')

    def validate_username(self, username):
        username = User.query.filter_by(username=username.data).first()
        if username:
            raise ValidationError('Пользователь с таким именем уже существует.') 
        
    def validate_email(self, email):
        user_log = User.query.filter_by(email=email.data).first()
        if user_log:
            raise ValidationError('Пользователь с таким email уже существует.')    

class LoginForm(FlaskForm):
    email = StringField('емаил', validators=[DataRequired(), Email()])
    password = PasswordField('пароль', validators=[DataRequired(), Length(min=6, max=100)])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired(), Length(min=2, max=150)])
    content = StringField('Содержание', validators=[DataRequired()])
    submit = SubmitField('Создать пост')
    
    def validate_title(self, title):
        post = Post.query.filter_by(title=title.data).first()
        if post:
            raise ValidationError('Пост с таким заголовком уже существует.')

