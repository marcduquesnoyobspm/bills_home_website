import os
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.utils import secure_filename

from ..utils.forms import (
    UpdateProfileIdentifiantForm,
    UpdateProfileImageForm,
    UpdateProfileInfosForm,
    UpdateProfilePasswordForm,
    DeleteProfileForm,
    UpdateProfileEmailForm,
)
from ..models import db
from ..models.user import User


user = Blueprint("user", __name__)


@user.route("/profile/", methods=["GET"])
@user.route("/profile", methods=["GET"])
@login_required
def profile_page():
    update_profile_identifiant_form = UpdateProfileIdentifiantForm()

    update_profile_image_form = UpdateProfileImageForm()

    update_profile_email_form = UpdateProfileEmailForm()

    update_profile_infos_form = UpdateProfileInfosForm()

    update_profile_password_form = UpdateProfilePasswordForm()

    delete_profile_form = DeleteProfileForm()

    if "user" in current_user.user_profile_picture:
        profile_pic_path = "images/upload/"

    else:
        profile_pic_path = "images/"

    return render_template(
        "profile.html",
        profile_pic_path=profile_pic_path,
        update_profile_identifiant_form=update_profile_identifiant_form,
        update_profile_email_form=update_profile_email_form,
        update_profile_image_form=update_profile_image_form,
        update_profile_infos_form=update_profile_infos_form,
        update_profile_password_form=update_profile_password_form,
        delete_profile_form=delete_profile_form,
    )


@user.route("/profile/update/infos", methods=["POST"])
@login_required
def update_user_infos():
    form = UpdateProfileInfosForm()

    if form.validate_on_submit():
        current_user.user_firstname = form.first_name.data

        current_user.user_lastname = form.last_name.data

        db.session.commit()

        return {
            "success": True,
            "first_name": current_user.user_firstname,
            "last_name": current_user.user_lastname,
        }

    return {"success": False}


@user.route("/profile/update/image", methods=["POST"])
@login_required
def update_user_picture():
    form = UpdateProfileImageForm()

    if form.validate_on_submit():
        f = form.image.data

        filename = secure_filename(f.filename)

        filename = (
            f"user_{current_user.id}_profile_pic{os.path.splitext(f.filename)[1]}"
        )

        if "user" in current_user.user_profile_picture:
            os.remove(
                os.path.join("static/images/upload/", current_user.user_profile_picture)
            )

        f.save(os.path.join("static/images/upload/", filename))

        current_user.user_profile_picture = filename

        db.session.commit()

        return {
            "success": True,
            "profile_picture": "static/images/upload/" + filename,
        }

    return {"success": False}


@user.route("/profile/update/identifiant", methods=["POST"])
@login_required
def update_user_identifiant():
    form = UpdateProfileIdentifiantForm()

    if form.validate_on_submit() and current_user.check_password(form.password.data):
        current_user.user_identifiant = form.identifiant.data

        db.session.commit()

        return {"success": True, "identifiant": current_user.user_identifiant}

    return {"success": False}


@user.route("/profile/update/email", methods=["POST"])
@login_required
def update_user_email():
    form = UpdateProfileEmailForm()

    if form.validate_on_submit() and current_user.check_password(form.password.data):
        current_user.user_email = form.email.data

        db.session.commit()

        return {"success": True, "email": current_user.user_email}

    return {"success": False}


@user.route("/profile/update/password", methods=["POST"])
@login_required
def update_user_password():
    form = UpdateProfilePasswordForm()

    if form.validate_on_submit() and current_user.check_password(
        form.current_password.data
    ):
        if form.future_password.data == form.current_password.data:
            return {"success": False}

        else:
            current_user.set_password(form.future_password.data)

            db.session.commit()

            return {"success": True}

    return {"success": False}


@user.route("/profile/delete", methods=["POST"])
@login_required
def delete_user():
    form = DeleteProfileForm()

    if form.validate_on_submit() and current_user.check_password(form.password.data):
        if "user" in current_user.user_profile_picture:
            os.remove(
                os.path.join("static/images/upload/", current_user.user_profile_picture)
            )

        db.session.delete(current_user)

        db.session.commit()

        return redirect(url_for("controllers.welcome.welcome_page"))

    return redirect(url_for("controllers.user.profile_page"))
