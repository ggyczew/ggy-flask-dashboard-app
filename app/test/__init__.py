from flask import Blueprint

bp = Blueprint(
    "test",
    __name__,
    url_prefix="/test",
    template_folder="templates",
    static_folder="static",
)
