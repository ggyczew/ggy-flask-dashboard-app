from app import create_app
import os
from . import services

app = create_app(os.getenv("FLASK_ENV") or "default")
app.app_context().push()


def kpi_update():
    app.logger.debug(f"Running KPI update task...")
    services.add_test_kpi_values()
    
    