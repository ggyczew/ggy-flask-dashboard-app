from . import bp
from flask import current_app as app
from flask import render_template
from app import db
from sqlalchemy import text


@bp.route("/oracle/", methods=["GET"])
def oracle_table_list():

    app.logger.debug("Testing...")

    engine = db.get_engine(bind="oracle")
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT table_name FROM all_tables")
        ).fetchall()

        # print(result)

    # Convert the list of tuples to a simple list of table names
    table_names = [table[0] for table in result]
    # table_names = ["raz", "dwa", "trzy"]

    return render_template(
        "oracle_table_list.html", tables=result, title="Oracle Table List"
    )
