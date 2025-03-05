from app import create_app
import os

app = create_app(os.getenv("FLASK_ENV") or "default")
app.app_context().push()


def task_run(id):

    app.logger.debug(f"Running task {id}...")
