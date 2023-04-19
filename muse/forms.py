from muse import m_app

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, HiddenField, SubmitField
from wtforms.validators import InputRequired, Length, NumberRange


class AddEmployee(FlaskForm):
    first_name = StringField('First Name', [InputRequired(), Length(min=3, max=50)])
    last_name = StringField('Last Name', [InputRequired(), Length(min=3, max=50)])
    address = StringField('Address', [InputRequired(), Length(min=3, max=125)])
    salary = IntegerField('Salary', [InputRequired(), NumberRange(min=500, max=10000)])
    submit = SubmitField('Add')


class UpdateEmployee(FlaskForm):
    f_name = StringField('First Name', [InputRequired(), Length(min=3, max=50)])
    l_name = StringField('Last Name', [InputRequired(), Length(min=3, max=50)])
    address = StringField('Address', [InputRequired(), Length(min=3, max=125)])
    salary = IntegerField('Salary', [InputRequired(), NumberRange(min=500, max=10000)])
    submit = SubmitField('Save')
