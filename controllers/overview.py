from flask import Blueprint, render_template, request
from flask_login import login_required


overview = Blueprint('overview', __name__)


@overview.route('/overview')
@login_required
def overview_page():
    tab = request.args.get('tab')
    if tab is None:
        tab = "overview"
    return render_template('overview.html', tab = tab)
    
