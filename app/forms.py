from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired, Length
from  flask_wtf.file import FileRequired


class partForm (FlaskForm):
    post = TextAreaField('Input your Part#...', validators=[DataRequired(), Length(min=1, max=120)])
    serv_lev = SelectField('Choose service level', choices=[('snt', '8x5xNBD'), ('snte', '8x5x4'), ('sntp', '24x7x4')])
    submit = SubmitField('Load')

class fileForm(FlaskForm):
    file = FileField('Choose file with part# or SKU',validators=[FileRequired()])
    levels = SelectField('Choose service level', choices=[('snt', '8x5xNBD'), ('snte', '8x5x4'), ('sntp', '24x7x4')])
    submit = SubmitField('Load')
