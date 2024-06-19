from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_maintenance.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)

    from mecha_manager.models import Part, Maintenance
    from mecha_manager.forms import PartForm, MaintenanceForm

    @app.route('/')
    def home():
        parts = Part.query.all()
        maintenances = Maintenance.query.all()
        return render_template('home.html', parts=parts, maintenances=maintenances)

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
                recommended_interval_mileage=form.recommended_interval_mileage.data
            )
            db.session.add(part)
            db.session.commit()
            return redirect(url_for('parts'))
        parts = Part.query.all()
        return render_template('parts.html', parts=parts, form=form)

    @app.route('/maintenance', methods=['GET', 'POST'])
    def maintenance():
        form = MaintenanceForm()
        if form.validate_on_submit():
            maintenance = Maintenance(
                date=form.date.data,
                part_id=form.part_id.data,
                mileage=form.mileage.data
            )
            db.session.add(maintenance)
            db.session.commit()
            return redirect(url_for('maintenance'))
        maintenances = Maintenance.query.all()
        return render_template('maintenance.html', maintenances=maintenances, form=form)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
