from __init__ import db

class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    part_number = db.Column(db.String(80), unique=True, nullable=False)
    photo = db.Column(db.String(120), nullable=True)
    price = db.Column(db.Float, nullable=False)
    purchase_link = db.Column(db.String(200), nullable=True)
    recommended_interval_time = db.Column(db.Integer, nullable=False)  # in months
    recommended_interval_mileage = db.Column(db.Integer, nullable=False)  # in miles
    category = db.Column(db.String(50), nullable=True)

class Maintenance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_of_replacement = db.Column(db.Date, nullable=False)
    part_id = db.Column(db.Integer, db.ForeignKey('part.id'), nullable=False)
    mileage_at_replacement = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(200), nullable=True)
    technician = db.Column(db.String(80), nullable=True)

class Setting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_mileage = db.Column(db.Integer, nullable=False)
    last_updated = db.Column(db.Date, nullable=False)
