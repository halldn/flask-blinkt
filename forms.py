from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired, InputRequired, NumberRange

class PulseForm(FlaskForm):
    red_value = IntegerField('Red Value', default=200, validators=[NumberRange(min=0, max=255), InputRequired("Please enter red value")])
    green_value = IntegerField('Green Value', default=200, validators=[NumberRange(min=0, max=255), InputRequired("Please enter green value")])
    blue_value = IntegerField('Blue Value', default=200, validators=[NumberRange(min=0, max=255), InputRequired("Please enter blue value")])
    step_count = IntegerField('Step Count', default=20, validators=[NumberRange(min=1, max=200), InputRequired("Please enter number of steps")])
    delay_time = DecimalField('Delay Time', places=2, default=0.01, validators=[NumberRange(min=0.009, max=1), InputRequired("Please enter time delay between steps")])
    submit = SubmitField('Pulse')
