import json


chart_config = {
    "type": "line",  # Chart type (changeable)
    "data": {
        "labels": [str(value.date) for value in kpi_values],  # X-axis labels
        "datasets": [{
            "label": f"KPI History - {kpi.title}",
            "data": [value.amount for value in kpi_values],  # Y-axis data
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

print(json.dumps(chart_config))