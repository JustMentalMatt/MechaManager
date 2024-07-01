from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_maintenance.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)

    from mecha_manager.models import Part, Maintenance, CurrentMileage
    from mecha_manager.forms import PartForm, MaintenanceForm, MileageForm

    @app.route('/')
    def home():
        parts = Part.query.all()
        maintenances = Maintenance.query.all()
        current_mileage = CurrentMileage.query.first()
        mileage_form = MileageForm()
        return render_template('home.html', parts=parts, maintenances=maintenances, current_mileage=current_mileage, mileage_form=mileage_form)

    @app.route('/update_mileage', methods=['POST'])
    def update_mileage():
        form = MileageForm()
        if form.validate_on_submit():
            current_mileage = CurrentMileage.query.first()
            if current_mileage:
                current_mileage.mileage = form.mileage.data
            else:
                current_mileage = CurrentMileage(mileage=form.mileage.data)
                db.session.add(current_mileage)
            db.session.commit()
        return redirect(url_for('home'))

    @app.route('/parts', methods=['GET', 'POST'])
    def parts():
        form = PartForm()
        if form.validate_on_submit():
            part = Part(
                name=form.name.data,
                part_number=form.part_number.data,
                photo_url=form.photo_url.data,
                price=form.price.data,
                purchase_link=form.purchase_link.data,
                recommended_interval_time=form.recommended_interval_time.data,
                recommended_interval_mileage=form.recommended_interval_mileage.data,
                additional_details=form.additional_details.data
            )
            db.session.add(part)
            db.session.commit()
            return redirect(url_for('parts'))
        parts = Part.query.all()
        return render_template('parts.html', parts=parts, form=form)

    @app.route('/part/<int:part_id>')
    def part_detail(part_id):
        part = Part.query.get_or_404(part_id)
        return render_template('part_detail.html', part=part)

    @app.route('/maintenance', methods=['GET', 'POST'])
    def maintenance():
        form = MaintenanceForm()
        if form.validate_on_submit():
            maintenance = Maintenance(
                date=form.date.data,
                part_id=form.part_id.data,
                mileage=form.mileage.data,
                additional_details=form.additional_details.data
            )
            db.session.add(maintenance)
            db.session.commit()
            return redirect(url_for('maintenance'))
        maintenances = Maintenance.query.all()
        return render_template('maintenance.html', maintenances=maintenances, form=form)

    @app.route('/maintenance/<int:maintenance_id>')
    def maintenance_detail(maintenance_id):
        maintenance = Maintenance.query.get_or_404(maintenance_id)
        return render_template('maintenance_detail.html', maintenance=maintenance)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
