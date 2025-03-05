from .models import Kpi
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


def get_kpi_by_id(kpi_id: int, order_by: str = "created_at") -> Kpi:
    kpi = Kpi.query.order_by(getattr(Kpi, order_by).desc()).filter_by(id=kpi_id).first()
    if kpi is None:
        raise ValueError(f"KPI with id {kpi_id} not found")
    return kpi

def get_kpi_by_name(kpi_name: str, order_by: str = "created_at") -> Kpi:
    kpi = Kpi.query.order_by(getattr(Kpi, order_by).desc()).filter_by(name=kpi_name).first()
    if kpi is None:
        raise ValueError(f"KPI with name '{kpi_name}' not found")
    return kpi

def get_most_recent_kpi(top: int = 1):
    kpis = Kpi.query.order_by(Kpi.created_at.desc()).limit(top).all()
    if not kpis:
        raise ValueError("No KPIs found")
    return kpis if top > 1 else kpis[0]