from . import bp
from flask import render_template, request, jsonify, redirect, url_for
from flask_security import current_user, auth_required, login_required, roles_accepted
from . import models, services


def is_xhr_request(request) -> bool:
    """ Utility function to check if XHR request """
    header = request.headers.get('X-Requested-With', None)
    if header is not None and header == 'XMLHttpRequest':
        return True
    return False


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


@bp.route('/kpi/<int:kpi_id>', methods=['GET'])
@login_required
# @roles_accepted('admin', 'staff')
def kpi_history(kpi_id):

    is_xhr = is_xhr_request(request)

    context = {
        'kpi_values': models.KpiValue.query.filter_by(kpi_id=kpi_id).all()
    }

    chart = request.args.get("chart", "false").lower() == "true"
    template = 'dashboard/kpi_history_chart.html' if chart else 'dashboard/kpi_history.html'

    return render_template(
        template,
        context=context,
        is_xhr=is_xhr,
        title=f'KPI History - {services.get_kpi(id=kpi_id).title}',
        legend=f'KPI History - {services.get_kpi(id=kpi_id).title}'
    )