from flask import render_template, request, redirect, url_for
from datetime import date
from __init__ import create_app, db
from models import Part, Maintenance, Setting

app = create_app()

@app.route('/')
def home():
    settings = Setting.query.first()
    parts = Part.query.all()
    overdue_parts = check_maintenance_due(parts, settings)
    return render_template('home.html', settings=settings, overdue_parts=overdue_parts)

@app.route('/parts')
def parts():
    parts = Part.query.all()
    return render_template('parts.html', parts=parts)

@app.route('/add_part', methods=['GET', 'POST'])
def add_part():
    if request.method == 'POST':
        new_part = Part(
            name=request.form['name'],
            part_number=request.form['part_number'],
            photo=request.form['photo'],
            price=request.form['price'],
            purchase_link=request.form['purchase_link'],
            recommended_interval_time=request.form['recommended_interval_time'],
            recommended_interval_mileage=request.form['recommended_interval_mileage'],
            category=request.form['category']
        )
        db.session.add(new_part)
        db.session.commit()
        return redirect(url_for('parts'))
    return render_template('add_part.html')

@app.route('/maintenance')
def maintenance():
    maintenance_logs = Maintenance.query.all()
    return render_template('maintenance.html', maintenance_logs=maintenance_logs)

@app.route('/add_maintenance', methods=['GET', 'POST'])
def add_maintenance():
    if request.method == 'POST':
        new_maintenance = Maintenance(
            date_of_replacement=request.form['date_of_replacement'],
            part_id=request.form['part_id'],
            mileage_at_replacement=request.form['mileage_at_replacement'],
            notes=request.form['notes'],
            technician=request.form['technician']
        )
        db.session.add(new_maintenance)
        db.session.commit()
        return redirect(url_for('maintenance'))
    parts = Part.query.all()
    return render_template('add_maintenance.html', parts=parts)

@app.route('/update_mileage', methods=['POST'])
def update_mileage():
    new_mileage = request.form['car_mileage']
    setting = Setting.query.first()
    if not setting:
        setting = Setting(car_mileage=new_mileage, last_updated=date.today())
        db.session.add(setting)
    else:
        setting.car_mileage = new_mileage
        setting.last_updated = date.today()
    db.session.commit()
    return redirect(url_for('home'))

def check_maintenance_due(parts, settings):
    overdue_parts = []
    today = date.today()
    current_mileage = settings.car_mileage if settings else 0

    for part in parts:
        maintenance_logs = Maintenance.query.filter_by(part_id=part.id).order_by(Maintenance.date_of_replacement.desc()).first()
        if maintenance_logs:
            time_diff = (today - maintenance_logs.date_of_replacement).days // 30  # Convert days to months
            mileage_diff = current_mileage - maintenance_logs.mileage_at_replacement

            if time_diff > part.recommended_interval_time or mileage_diff > part.recommended_interval_mileage:
                overdue_parts.append(part)
        else:
            overdue_parts.append(part)
    
    return overdue_parts
