from flask import Blueprint

bp = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/dashboard",
    template_folder="templates", 
    static_folder="static"
)

from . import filters
from . import models
from . import routes
from . import scripts