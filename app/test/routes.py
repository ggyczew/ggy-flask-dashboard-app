from . import bp
from flask import current_app as app
from flask import render_template
from app import db
from sqlalchemy import text
import pandas as pd


@bp.route("/oracle/", methods=["GET"])
def oracle_table_list():

    app.logger.debug("Testing...")

    engine = db.get_engine(bind="oracle")
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT table_name FROM all_tables")
        ).fetchall()

    return render_template(
        "oracle_table_list.html", tables=result, title="Oracle Table List"
    )


@bp.route("/sqlite/", methods=["GET"])
def sqlite_table_list():

    app.logger.debug("Testing PANDAS to RESULT...")

    with db.get_engine().connect() as connection:
        result = pd.read_sql(text("SELECT * FROM users"), connection).to_dict(orient="records")
    
    return render_template(
        "sqlite_users_list.html", users=result, title="SQLITE Table List"
    )
