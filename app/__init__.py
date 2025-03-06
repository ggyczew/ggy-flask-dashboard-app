from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore
from flask_debugtoolbar import DebugToolbarExtension
from flask_apscheduler import APScheduler
from sqlalchemy import MetaData

from .commands import commands
from config import config


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
scheduler = APScheduler()
toolbar = DebugToolbarExtension()


def register_extensions(app):

    db.init_app(app)
    if db.engine.url.drivername == "sqlite":
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    from .core.models import User, Role

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    if app.config.get("SHOW_FLASK_DEBUG_TOOLBAR", False):
        toolbar.init_app(app)


def register_blueprints(app):
    from importlib import import_module

    for module_name in ["core", "dashboard"]:
        module = import_module(f"app.{module_name}.routes")
        app.register_blueprint(module.bp)


def configure_redis_queue(app):
    from redis import Redis
    from rq import Queue

    redis_host = app.config.get("RQ_REDIS_HOST", None)
    redis_port = app.config.get("RQ_REDIS_PORT", None)
    app.redis = Redis(host=redis_host, port=redis_port)
    app.task_queue = Queue("app-tasks", connection=app.redis)


def configure_rq_dashboard(app):
    import rq_dashboard

    app.config.from_object(rq_dashboard.default_settings)
    rq_dashboard.web.setup_rq_connection(app)
    app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")


def configure_scheduler(app):
    scheduler.init_app(app)
    scheduler.start()


def configure_commands(app):
    app.register_blueprint(commands)


def page_not_found(e):
    return render_template("404.html"), 404


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_error_handler(404, page_not_found)

    with app.app_context():
        register_extensions(app)
        register_blueprints(app)

        configure_redis_queue(app)
        configure_rq_dashboard(app)
        configure_scheduler(app)

        # Define the custom commands
        configure_commands(app)

        db.create_all(bind_key=[None])

    return app
