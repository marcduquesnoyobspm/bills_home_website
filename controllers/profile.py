from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, login_required


profile = Blueprint('profile', __name__)

@profile.route('/profile')
@login_required
def profile_page():
    return render_template('profile.html')