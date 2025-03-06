from . import bp
from flask import render_template
from flask_security import current_user, auth_required, login_required, roles_accepted
from . import models, services


@bp.route("/")
# @auth_required()
def index():

    context = {
        'kpis': [
            services.get_kpi(id=1),
            services.get_kpi(id=2),
            services.get_kpi(id=3),
        ]
    }

    return render_template(
        "dashboard/index.html",
        title="Dashboard",
        legend="Dashboard",
        context=context,
    )