from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from ..forms import RegisterForm, LoginForm
from ..extensions import db, bcrypt
from ..models.user import User
from ..function import save_picture
from flask_login import login_user, logout_user, login_required 


user = Blueprint('user',__name__)

@user.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        password_hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        avatar_filename = save_picture(form.avatar.data)    
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=password_hashed,
            avatar = avatar_filename
        )

        try:
            db.session.add(user)
            db.session.commit()
            flash('Вы успешно зарегистрированы!', 'success')
            return redirect(url_for('user.login'))
        except Exception as e:
            print(str(e))
            flash(f'Ошибка регистрации: {str(e)}', 'danger')
            return redirect(url_for('user.register'))
    return render_template('user/register.html', form=form)        

@user.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('Вы успешно вошли в систему!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Неверный email или пароль.', 'danger')  
    return render_template('user/login.html', form=form)

@user.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash('Вы вышли из системы.', 'success')
    return redirect(url_for('main.index'))