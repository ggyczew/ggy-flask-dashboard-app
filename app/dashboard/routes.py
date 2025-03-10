from . import bp
from flask import render_template, request, jsonify, redirect, url_for
from flask_security import current_user, auth_required, login_required, roles_accepted
from . import models, services
from flask import current_app as app

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
    """Fetch KPI history, returning JSON for charts or rendering HTML for the dashboard."""
    
    # Check if the request is an XHR request
    is_xhr = is_xhr_request(request)

    kpi = services.get_kpi(id=kpi_id)
    kpi_values = models.KpiValue.query.filter_by(kpi_id=kpi_id).all()

    if request.args.get("chart", "0") == "1":
        chart_config = {'X': 'Y'}
        chart_config = {
            "type": "line",  # Chart type (changeable)
            "data": {
                "labels": [str(v.created_at) for v in kpi_values],  # X-axis labels
                "datasets": [{
                    "label": f"KPI History - {kpi.title}",
                    "data": [v.value for v in kpi_values],  # Y-axis data
                    "backgroundColor": "rgba(75, 192, 192, 0.2)",
                    "borderColor": "rgba(75, 192, 192, 1)",
                    "borderWidth": 2,
                    "fill": True
                }]
            },
            "options": {
                "responsive": True,
                "maintainAspectRatio": False,
                "scales": {
                    "x": {"title": {"display": True, "text": "Date"}},
                    "y": {"title": {"display": True, "text": "Value"}}
                },
                "plugins": {
                    "legend": {"position": "top"}
                }
            }
        }
        app.logger.debug(chart_config)
        return jsonify(chart_config)


    context = {'kpi_values': kpi_values}

    return render_template(
        'dashboard/kpi_history.html',
        context=context,
        is_xhr=is_xhr,
        title=f'KPI History - {kpi.title}',
        legend=f'KPI History - {kpi.title}'
    )