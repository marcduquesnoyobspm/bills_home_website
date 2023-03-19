from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, login_required


overview = Blueprint('overview', __name__)

@overview.route('/overview')
@login_required
def overview_page():
    return render_template('overview.html')