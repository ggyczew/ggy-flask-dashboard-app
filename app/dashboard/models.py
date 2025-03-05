from enum import unique
from app import db


class Kpi(db.Model):
    __tablename__ = "kpi"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    value = db.Column(db.Float, nullable=False)
    target = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(255), nullable=False)
    icon = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return f"<Kpi {self.name}>"