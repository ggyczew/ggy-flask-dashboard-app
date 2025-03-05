from app import create_app
import os
from services import kpi_generate_test_data

app = create_app(os.getenv("FLASK_ENV") or "default")
app.app_context().push()


def kpi_update(id):
    # with app.app_context():
    app.logger.debug(f"Running KPI update task...")
    # kpi_generate_test_data()
    
    