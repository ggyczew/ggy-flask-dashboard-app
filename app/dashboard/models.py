from app import db

class Kpi(db.Model):
    __tablename__ = "kpi"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    unit = db.Column(db.String(255), nullable=False)
    icon = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return f"<Kpi {self.name}>"
    
    @property
    def current_value(self):
        return KpiValue.query.filter_by(kpi_id=self.id).order_by(KpiValue.created_at.desc()).first()

class KpiValue(db.Model):
    __tablename__ = "kpi_value"
    id = db.Column(db.Integer, primary_key=True)
    kpi_id = db.Column(db.Integer, db.ForeignKey('kpi.id'), nullable=False)
    value = db.Column(db.Float, nullable=False)
    target = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    kpi = db.relationship('Kpi', backref=db.backref('values', lazy=True))

    def __repr__(self):
        return f"<KpiValue {self.value} for Kpi {self.kpi_id}>"