from flask import current_app as app
from app import scheduler


@scheduler.task("interval", id="task_run_job", seconds=20, misfire_grace_time=900)
def task_enqueue():
    """Run pending tasks. Triggered by Scheduler"""

    with scheduler.app.app_context():
        app.logger.debug("Scheduled task run ...")
        app.task_queue.enqueue("app.test.tasks.task_run", 1)
