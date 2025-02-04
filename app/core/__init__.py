from flask import Blueprint

bp = Blueprint(
    "core", __name__, url_prefix="", template_folder="templates", static_folder="static"
)

from . import filters
from . import models
from . import routes
