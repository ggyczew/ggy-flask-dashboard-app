from flask import current_app as app
from app import db, scheduler


def task_run(id):
    app.logger.debug(f"Running task {id}...")


@scheduler.task("interval", id="task_run_job", seconds=20, misfire_grace_time=900)
def task_enqueue():
    """Run pending tasks. Triggered by Scheduler"""

    app.logger.debug("Enqueing task...")

    # with scheduler.app.app_context():
    #     app.logger.debug("Scheduled task run ...")
    #     app.task_queue.enqueue("app.rpt.tasks.run_task", 1)
