import os
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user, login_user, logout_user
from ..utils.forms import OverviewUpdateProfileForm
from ..models import db
from ..models.user import User


overview = Blueprint("overview", __name__)


@overview.route("/overview")
@login_required
def overview_page():
    form = OverviewUpdateProfileForm()

    tab = request.args.get("tab")

    if tab is None:
        tab = "overview"

    if "user" in current_user.user_profile_picture:
        profile_pic_path = "images/upload/"

    else:
        profile_pic_path = "images/"

    return render_template(
        "overview.html", form=form, profile_pic_path=profile_pic_path, tab=tab
    )


@overview.route("/overview/update/profile", methods=["POST"])
@login_required
def overview_update_profile():
    form = OverviewUpdateProfileForm()

    if form.validate_on_submit():
        current_user.user_firstname = form.first_name.data

        current_user.user_lastname = form.last_name.data

        db.session.commit()

        modified_user = User.query.get(current_user.id)

        login_user(modified_user)

        return {
            "success": True,
            "first_name": current_user.user_firstname,
            "last_name": current_user.user_lastname,
        }

    return {"success": False}
