from flask import current_app as app
from app import scheduler


@scheduler.task("interval", id="kpi_update_job", seconds=60, misfire_grace_time=900)
def task_enqueue():
    """Run pending tasks. Triggered by Scheduler"""

    with scheduler.app.app_context():
        app.logger.debug("Scheduled KPI update ...")
        app.task_queue.enqueue("app.dashboard.tasks.kpi_update", 1)
