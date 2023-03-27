from flask import Blueprint, render_template, flash, redirect, url_for, session
from flask_login import current_user, login_user, login_required
from ..utils.forms import StartRegistrationForm


welcome = Blueprint('welcome', __name__)


@welcome.route('/', methods=['GET', 'POST'])
def welcome_page():

    if current_user.is_authenticated:

        return redirect(url_for('overview.overview_page'))

    form = StartRegistrationForm()

    if form.validate_on_submit():

        session['user_email'] = form.email.data

        return redirect(url_for('auth.register_more_infos'))

    return render_template('welcome.html', form=form)
