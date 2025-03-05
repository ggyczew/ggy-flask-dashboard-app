from . import bp
from time import strftime

# Custom Jinja template filters
@bp.app_template_filter('format_date')
def format_date(value, format='%Y-%m-%d'):
    """Format a date time to (Default): yyyy-mm-dd"""
    if value is None:
        return ""
    return value.strftime(format)

@bp.app_template_filter('format_datetime')
def format_datetime(value, format='%Y-%m-%d %H:%M:%S'):
    """Format a date time to (Default): yyyy-mm-dd hh:mm:ss"""
    if value is None:
        return ""
    return value.strftime(format)


@bp.app_template_filter('format_percentage')
def format_percentage(value, format='{:.2f}%'):
    """Format a float to percentage"""
    if value is None:
        return ""
    return format.format(value)

