import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):

    DEBUG = os.environ.get("DEBUG")

    ADMINS = frozenset(["admin@localhost"])
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-key"
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

    CSRF_ENABLED = True
    CSRF_SESSION_KEY = os.environ.get("CSRF_SESSION_KEY")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # As of Flask-SQLAlchemy 2.4.0 it is easy to pass in options directly to the
    # underlying engine. This option makes sure that DB connections from the pool
    # are still valid. Important for entire application since many DBaaS options
    # automatically close idle connections.
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_pre_ping": True}
    SQLALCHEMY_RECORD_QUERIES = True

    SECURITY_TRACKABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_PASSWORD_HASH = "argon2"
    SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT")
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_POST_LOGOUT_VIEW = "/loggedout"

    SCHEDULE_TASK_DAYS_AHEAD = 2
    SCHEDULE_TASK_UPDATE_INTERVAL = 300
    SCHEDULE_TASK_RUN_INTERVAL = 600

    RQ_REDIS_HOST = os.environ.get("RQ_REDIS_HOST")
    RQ_REDIS_PORT = os.environ.get("RQ_REDIS_PORT")
    RQ_DASHBOARD_REDIS_URL = f"redis://{RQ_REDIS_HOST}:{RQ_REDIS_PORT}"

    DEBUG_TB_INTERCEPT_REDIRECTS = False
    #  !!! TODO Duplicate !!! see SQLALCHEMY_BINDS
    DATASOURCE_DATABASE_URI = "sqlite:///" + os.path.join(
        basedir, "data", "data.sqlite"
    )

    REPORTS_DIR = os.path.join(basedir, "reports")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "sqlite:///" + os.path.join(basedir, "app.sqlite")
    )
    SQLALCHEMY_BINDS = {
        "datasource": "sqlite:///" + os.path.join(basedir, "data", "data.sqlite"),
        "oracle": os.getenv("ORACLE_DATABASE_URL"),
    }


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.sqlite")
    SQLALCHEMY_BINDS = {
        "datasource": "sqlite:///" + os.path.join(basedir, "data", "data.sqlite"),
        "oracle": os.getenv("ORACLE_DATABASE_URL"),
    }


class DevelopmentFDTConfig(Config):
    SHOW_FLASK_DEBUG_TOOLBAR = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.sqlite")
    SQLALCHEMY_BINDS = {
        "datasource": "sqlite:///" + os.path.join(basedir, "data", "data.sqlite"),
        "oracle": os.getenv("ORACLE_DATABASE_URL"),
    }


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "testing_app.sqlite")
    SQLALCHEMY_BINDS = {
        "datasource": "sqlite:///" + os.path.join(basedir, "data", "data.sqlite"),
        "oracle": os.getenv("ORACLE_DATABASE_URL"),
    }


config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "developmentFDT": DevelopmentFDTConfig,
    "testing": TestingConfig,
    "default": DevelopmentFDTConfig,
}
