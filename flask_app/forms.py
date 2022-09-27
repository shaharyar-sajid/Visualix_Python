from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField

class CsvForm(FlaskForm):
    csv = FileField('CSV File needed', validators=[FileRequired()], name='file')
    submit = SubmitField('Upload File')