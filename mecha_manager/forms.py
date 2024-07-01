from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, URLField, DateField, TextAreaField
from wtforms.validators import DataRequired, URL

class PartForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    part_number = StringField('Part Number', validators=[DataRequired()])
    photo_url = URLField('Photo URL', validators=[URL()])
    price = FloatField('Price', validators=[DataRequired()])
    purchase_link = URLField('Purchase Link', validators=[URL()])
    recommended_interval_time = IntegerField('Recommended Interval (months)')
    recommended_interval_mileage = IntegerField('Recommended Interval (miles)')
    additional_details = TextAreaField('Additional Details')
    submit = SubmitField('Add Part')

class MaintenanceForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    part_id = IntegerField('Part ID', validators=[DataRequired()])
    mileage = IntegerField('Mileage', validators=[DataRequired()])
    additional_details = TextAreaField('Additional Details')
    submit = SubmitField('Add Maintenance')

class MileageForm(FlaskForm):
    mileage = IntegerField('Mileage', validators=[DataRequired()])
    submit = SubmitField('Update Mileage')
