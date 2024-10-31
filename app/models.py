from . import db
from datetime import datetime, timezone
import uuid

class Paciente(db.Model):
    __tablename__ = 'pacientes'
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    run = db.Column(db.String(12), unique=True, nullable=False)
    historia = db.Column(db.Text, nullable=True)
    creado_en = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    atenciones = db.relationship('Atencion', backref='paciente', lazy=True)

class Atencion(db.Model):
    __tablename__ = 'atenciones'
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    paciente_id = db.Column(db.String, db.ForeignKey('pacientes.id'), nullable=False)
    detalle = db.Column(db.Text, nullable=True)
    creado_en = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))