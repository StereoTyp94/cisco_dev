from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class partForm (FlaskForm):
    post = TextAreaField('Input your Part#...', validators=[DataRequired(), Length(min=1, max=120)])
    submit = SubmitField('Load')
