from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, login_required, logout_user
from ..models import db
from ..models.user import User
from ..utils.forms import LoginForm, RegistrationForm


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


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('overview.overview_page'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(user_email=form.email.data, user_identifiant=form.identifiant.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=form.remember_me.data)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('overview.overview_page'))
    return render_template('register.html', title='Register', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('welcome.welcome_page'))
