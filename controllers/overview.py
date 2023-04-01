from flask import Blueprint, render_template, request
from flask_login import login_required, current_user, login_user, logout_user
from ..utils.forms import OverviewUpdateProfileForm
from ..models import db


overview = Blueprint('overview', __name__)


@overview.route('/overview')
@login_required
def overview_page():
    
    form = OverviewUpdateProfileForm()
    
    tab = request.args.get('tab')
    
    if tab is None:
    
        tab = "overview"
    
    return render_template('overview.html', form = form, tab = tab)
    

@overview.route('/overview/update/profile', methods=["POST"])
@login_required
def overview_update_profile():
    
    form = OverviewUpdateProfileForm()
    
    if form.validate_on_submit():
        
        current_user.user_firstname = form.first_name.data
        
        current_user.user_lastname = form.last_name.data
        
        db.session.commit()
        
        User.query.get(int(id))
        
        login_user(current_user)
        
        return {"success":True}
    
    return {"success":False}