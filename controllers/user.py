from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from ..utils.forms import UpdateProfileForm
from ..models import db

user = Blueprint('user', __name__)


@user.route('/profile', methods=['GET','POST'])
@login_required
def profile_page():
    form = UpdateProfileForm()
    """ if form.validate_on_submit() and current_user.check_password(form.current_password.data):
        current_user.user_identifiant = form.identifiant.data
        current_user.user_firstname = form.first_name.data
        current_user.user_lastname = form.last_name.data
        current_user.user_email = form.email.data
        current_user.set_password(form.future_password.data)
        db.session.add(current_user)
        db.session.commit() """
    return render_template('profile.html', form = form, user = current_user)


@user.route('/profile/update', methods=['GET','POST'])
@login_required
def update_user():
    form = UpdateProfileForm()
    if form.validate_on_submit() and current_user.check_password(form.current_password.data):
        current_user.user_identifiant = form.identifiant.data
        current_user.user_firstname = form.first_name.data
        current_user.user_lastname = form.last_name.data
        current_user.user_email = form.email.data
        current_user.set_password(form.future_password.data)
        db.session.commit()
        return redirect(url_for('controllers.user.profile_page'))
    return render_template('profile.html', form = form, user = current_user)
    

@user.route('/profile/delete', methods=['GET'])
@login_required
def delete_user():
    db.session.delete(current_user)
    db.session.commit()
    return redirect(url_for('controllers.overview.overview_page'))