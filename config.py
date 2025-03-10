import os
from dotenv import load_dotenv
import logging

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):

    DEBUG = os.environ.get("DEBUG")

    ADMINS = frozenset(["admin@me.com"])
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-key"
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

    CSRF_ENABLED = True
    CSRF_SESSION_KEY = os.environ.get("CSRF_SESSION_KEY")

    # have session and remember cookie be samesite (flask/flask_login)
    REMEMBER_COOKIE_SAMESITE = "strict"
    SESSION_COOKIE_SAMESITE = "strict"

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

    SCHEDULER_API_ENABLED = True

    RQ_REDIS_HOST = os.environ.get("RQ_REDIS_HOST")
    RQ_REDIS_PORT = os.environ.get("RQ_REDIS_PORT")
    RQ_DASHBOARD_REDIS_URL = f"redis://{RQ_REDIS_HOST}:{RQ_REDIS_PORT}"

    DEBUG_TB_INTERCEPT_REDIRECTS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_BINDS = {
        "datasource": "sqlite:///" + os.path.join(basedir, "data", "data.sqlite"),
        "oracle": os.getenv("ORACLE_DATABASE_URL"),
    }


class DevelopmentConfig(Config):
    SHOW_FLASK_DEBUG_TOOLBAR = True
    DEBUG = True
    LOGGING_LEVEL = logging.DEBUG
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_BINDS = {
        "datasource": "sqlite:///" + os.path.join(basedir, "data", "data.sqlite"),
        "oracle": os.getenv("ORACLE_DATABASE_URL"),
    }


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_BINDS = {
        "datasource": "sqlite:///" + os.path.join(basedir, "data", "data.sqlite"),
        "oracle": os.getenv("ORACLE_DATABASE_URL"),
    }


config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
