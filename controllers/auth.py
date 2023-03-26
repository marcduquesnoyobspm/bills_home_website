from flask import Blueprint, render_template, flash, redirect, url_for, session
from flask_login import login_user, login_required, logout_user, current_user
from ..models import db
from ..models.user import User
from ..utils.forms import LoginForm, PasswordRegistrationForm, FinalRegistrationForm


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('overview.overview_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('overview.overview_page'))
    return render_template('login.html', title='Log In', form=form)


@auth.route('/signup/password', methods=['GET', 'POST'])
def register_password():
    if current_user.is_authenticated:
        return redirect(url_for('overview.overview_page'))
    form = PasswordRegistrationForm()
    if form.validate_on_submit():
        user_to_register = User()
        user_to_register.set_password(form.password.data)
        session['user_password'] = user_to_register.user_password
        return redirect(url_for('auth.register_more_infos'))
    return render_template('register.html', form = form, step = 2)


@auth.route('/signup/more_infos', methods=['GET', 'POST'])
def register_more_infos():
    if current_user.is_authenticated:
        return redirect(url_for('overview.overview_page'))
    form = FinalRegistrationForm()
    if form.validate_on_submit():
        user_to_register = User(
            user_email = session['user_email'],
            user_password = session['user_password'],
            user_identifiant=form.identifiant.data,
            user_firstname=form.first_name.data,
            user_lastname=form.last_name.data
        )
        db.session.add(user_to_register)
        db.session.commit()
        login_user(user_to_register, remember=form.remember_me.data)
        session.pop('user_email', None)
        session.pop('user_password', None)
        return redirect(url_for('overview.overview_page'))
    return render_template('register.html', form = form, step = 3)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('welcome.welcome_page'))
