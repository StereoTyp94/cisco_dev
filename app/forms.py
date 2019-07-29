from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length


class partForm (FlaskForm):
    post = TextAreaField('Input your Part#...', validators=[DataRequired(), Length(min=1, max=120)])
    # serv_lev = SelectField(choices=[('snt', '8x5xNBD'), ('snte', '8x5x4'), ('sntp', '24x7x4')])
    submit = SubmitField('Load')
