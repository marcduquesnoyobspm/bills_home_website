from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from ..models import db
from ..models.user import User
from ..utils.forms import RegistrationForm

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('overview'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(user_email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@auth.route('/logout')
def logout():
    return 'Logout'
