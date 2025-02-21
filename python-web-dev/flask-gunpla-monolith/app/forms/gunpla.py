from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class GunplaForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    series = StringField('Series', validators=[DataRequired()])
    grade = StringField('Grade', validators=[DataRequired()])
    scale = StringField('Scale')
    submit = SubmitField('Submit')