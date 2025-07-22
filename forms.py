from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length

class ComplaintForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    category = SelectField("Category", choices=[
        ('Billing', 'Billing'), 
        ('Service', 'Service'), 
        ('Product', 'Product'), 
        ('Other', 'Other')
    ], validators=[DataRequired()])
    complaint = TextAreaField("Complaint", validators=[DataRequired(), Length(min=15)])
