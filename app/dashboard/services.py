from .models import Kpi, KpiValue
from app import db
import random

def add_test_kpi():
    test_kpis = [
        Kpi(name="Revenue", title="Revenue", description="Total revenue generated", unit="$", icon="revenue_icon.png"),
        Kpi(name="Customer Satisfaction", title="Customer Satisfaction", description="Customer satisfaction score", unit="%", icon="satisfaction_icon.png"),
        Kpi(name="Employee Productivity", title="Employee Productivity", description="Average tasks completed per employee", unit="tasks", icon="productivity_icon.png")
    ]
    
    db.session.bulk_save_objects(test_kpis)
    db.session.commit()

def add_test_kpi_values():
    
    if Kpi.query.count() == 0:
        add_test_kpi()  # Ensure KPIs are added only once
    
    test_kpi_values = [
        KpiValue(kpi_id=1, value=random.uniform(40000, 60000), target=60000),
        KpiValue(kpi_id=2, value=random.uniform(75, 95), target=90),
        KpiValue(kpi_id=3, value=random.uniform(20, 30), target=30)
    ]
    
    db.session.bulk_save_objects(test_kpi_values)
    db.session.commit()

def get_kpi(*, id: int = None, name: str = None) -> Kpi:
    
    if id is not None:
        kpi = Kpi.query.filter_by(id=id).first()
    elif name is not None:
        kpi = Kpi.query.filter_by(name=name).first()
    else:
        raise ValueError("Either id or name must be provided")
    if kpi is None:
        raise ValueError("KPI not found")
    return kpi


