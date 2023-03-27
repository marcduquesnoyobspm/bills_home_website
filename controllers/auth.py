from flask import Blueprint, render_template, flash, redirect, url_for, session, request
from flask_login import login_user, login_required, logout_user, current_user
import datetime
from ..models import db
from ..models.user import User
from ..utils.forms import LoginForm, MoreInfosRegistrationForm, FinalRegistrationForm


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
@auth.route('/login/', methods=['GET', 'POST'])
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


@auth.route('/signup', methods=['GET'])
@auth.route('/signup/', methods=['GET'])
def register():
    
    more_infos_form = MoreInfosRegistrationForm()
    
    password_form = FinalRegistrationForm()
    
    if current_user.is_authenticated:
    
        return redirect(url_for('overview.overview_page'))
    
    else:
    
        if session.get('user_email') is None:
            
            return redirect(url_for('welcome.welcome_page'))
        
        elif session.get('user_identifiant') is not None:
            
                return render_template('register.html', more_infos_form = more_infos_form, password_form = password_form, step = 3)
        
    return render_template('register.html', more_infos_form = more_infos_form, password_form = password_form, step = 2)
    
    
@auth.route('/signup/more_infos', methods=['POST'])
@auth.route('/signup/more_infos/', methods=['POST'])
def register_more_infos():
    
    more_infos_form = MoreInfosRegistrationForm()
    
    if current_user.is_authenticated:
    
        return redirect(url_for('overview.overview_page'))
    
    else:
    
        if session.get('user_email') is None:
            
            return redirect(url_for('welcome.welcome_page'))
        
        elif session.get('user_identifiant') is not None:
            
            return redirect(url_for('auth.register'))

    if more_infos_form.validate_on_submit():
    
        session["user_identifiant"] = more_infos_form.identifiant.data
    
        session["user_firstname"] = more_infos_form.first_name.data

        session["user_lastname"] = more_infos_form.last_name.data
        
        return {"success" : True}
    
    return {"success" : False}


@auth.route('/signup/password', methods=['POST'])
@auth.route('/signup/password/', methods=['POST'])
def register_password():
    
    password_form = FinalRegistrationForm()
    
    if current_user.is_authenticated:
        
        return redirect(url_for('overview.overview_page'))
    
    else:
    
        if session.get('user_email') is None:
            
            return redirect(url_for('welcome.welcome_page'))
        
        elif session.get('user_identifiant') is None:
    
            return redirect(url_for('auth.register'))
    
    if password_form.validate_on_submit():
        
        user_to_register = User(
    
            user_email = session['user_email'],
    
            user_identifiant = session["user_identifiant"],
    
            user_firstname = session["user_firstname"],
    
            user_lastname = session["user_lastname"],
    
            user_creation_date = datetime.date.today()
    
        )
    
        user_to_register.set_password(password_form.password.data)
        
        db.session.add(user_to_register)
    
        db.session.commit()
    
        login_user(user_to_register, remember=password_form.remember_me.data)
    
        session.pop('user_email', None)
            
        session.pop('user_identifiant', None)
        
        session.pop('user_firstname', None)

        session.pop('user_lastname', None)
    
        return redirect(url_for('overview.overview_page'))


@auth.route('/logout')
@auth.route('/logout/')
@login_required
def logout():
    
    logout_user()
    
    return redirect(url_for('welcome.welcome_page'))