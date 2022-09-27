import os
from flask import Flask, render_template, request, redirect, url_for, abort
from flask_app import app
from werkzeug.utils import secure_filename
import pandas as pd
from visualizations import util, flask_visual
from flask_app.forms import CsvForm

# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template('index.html', title='Home')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def upload_files():
    if request.method == 'POST':
        df = None
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            uploaded_file.stream.seek(0) # seek to the beginning of file
            #df = pd.read_csv(uploaded_file.stream)
            df = util.load_stream_file(uploaded_file.stream)
            util.split_title(df)
            util.split_date(df)
            util.make_day_categorical(df)
            day_fig = flask_visual.visual_day_activity(df)
        #return render_template('index.html', title='Home', tables=[df.to_html(classes='data')], titles=df.columns.values, day_fig=day_fig)
        return render_template('index.html', title='Home', day_fig=day_fig)

    return render_template('index.html', title='Home')