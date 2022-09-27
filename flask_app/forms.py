from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField

class CsvForm(FlaskForm):
    photo = FileField(validators=[FileRequired()])
    submit = SubmitField('Upload File')