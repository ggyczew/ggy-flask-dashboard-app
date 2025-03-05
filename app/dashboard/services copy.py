from models import Kpi
from app import db
import random

def kpi_generate_test_data():
    test_kpis = [
        Kpi(name="Revenue", description="Total revenue generated", value=random.uniform(40000, 60000), target=60000, unit="$", icon="revenue_icon.png"),
        Kpi(name="Customer Satisfaction", description="Customer satisfaction score", value=random.uniform(75, 95), target=90, unit="%", icon="satisfaction_icon.png"),
        Kpi(name="Employee Productivity", description="Average tasks completed per employee", value=random.uniform(20, 30), target=30, unit="tasks", icon="productivity_icon.png")
    ]
    
    db.session.bulk_save_objects(test_kpis)
    db.session.commit()


def get_kpi_by_id(kpi_id: int) -> Kpi:
    kpi = Kpi.query.get(kpi_id)
    if kpi is None:
        raise ValueError(f"KPI with id {kpi_id} not found")
    return kpi

def get_kpi_by_name(kpi_name: str) -> Kpi:
    kpi = Kpi.query.filter_by(name=kpi_name).first()
    if kpi is None:
        raise ValueError(f"KPI with name '{kpi_name}' not found")
    return kpi

