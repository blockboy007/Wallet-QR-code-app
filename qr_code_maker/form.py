from flask_wtf import FlaskForm
from wtforms import (StringField, SelectField, SubmitField)
from wtforms.validators import DataRequired


class InfoForm(FlaskForm):
    address = StringField(
        'Please input your wallet address', validators=[DataRequired()])
    chain = SelectField('Pick your blockchain:', choices=[
                        ('bsc', 'BSC'), ('avax', 'AVAX'), ('eth', 'ETH'), ('ada', 'ADA')])
    submit = SubmitField('Submit')
