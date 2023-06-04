from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField

class CsvForm(FlaskForm):
    '''
    Form for uploading csv file

    Parameters
    ----------
    FlaskForm : object
        FlaskForm object
    '''

    csv = FileField('CSV File needed', validators=[FileRequired()], name='file')
    submit = SubmitField('Upload File')