from flask import Blueprint, render_template
from flask_login import login_required


overview = Blueprint('overview', __name__)


@overview.route('/overview')
@login_required
def overview_page():
    return render_template('overview.html')
