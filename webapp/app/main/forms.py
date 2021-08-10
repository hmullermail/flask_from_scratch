from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length, NumberRange


class MyTable_Form(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    value = StringField('Value', validators=[DataRequired()])
    submit = SubmitField('Record')
