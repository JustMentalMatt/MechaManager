from mecha_manager.app import db
import datetime

class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    part_number = db.Column(db.String(100), unique=True, nullable=False)
    photo_url = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Float, nullable=False)
    purchase_link = db.Column(db.String(200), nullable=True)
    recommended_interval_time = db.Column(db.Integer, nullable=True)
    recommended_interval_mileage = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<Part {self.name}>'

class Maintenance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.UTC)
    part_id = db.Column(db.Integer, db.ForeignKey('part.id'), nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    part = db.relationship('Part', backref=db.backref('maintenances', lazy=True))

    def __repr__(self):
        return f'<Maintenance {self.date}>'
