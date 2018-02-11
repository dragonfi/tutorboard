from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class NewTaskForm(FlaskForm):
    description = TextAreaField('description', validators=[DataRequired()])


class NewSolutionForm(FlaskForm):
    solution = TextAreaField('solution', validators=[DataRequired()])
