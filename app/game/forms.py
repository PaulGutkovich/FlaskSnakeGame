from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField

class SaveScoreForm(FlaskForm):
    save_score = BooleanField("Would You Like To Save Your Score?")
    submit = SubmitField("Submit")