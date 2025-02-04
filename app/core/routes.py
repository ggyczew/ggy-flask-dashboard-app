from . import bp
from flask import render_template
from flask_security import current_user, auth_required, login_required, roles_accepted
from . import models


@bp.route("/")
@auth_required()
def index():
    return render_template("index.html")


@bp.route("/loggedout")
def loggedout():
    return render_template("loggedout.html")


@bp.route("/profile")
@auth_required()
@roles_accepted("admin", "staff", "user")
def profile_detail():
    profile = current_user
    return render_template(
        "profile_detail.html", profile=profile, title="My Profile", legend="My Profile"
    )


@bp.route("/profile/update")
@auth_required()
@roles_accepted("admin", "staff", "user")
def profile_update():
    profile = current_user
    return render_template(
        "profile_form.html",
        profile=profile,
        title="Edit Profile",
        legend="Edit Profile",
    )
