from pathlib import Path

from flask import Flask
from flask import flash, request, redirect, url_for, render_template

from werkzeug.utils import secure_filename
from datetime import datetime
import re

import os

hostname = os.uname()[1]
# hostname = 'Khang'

ALLOWED_EXTENSIONS = {'csv'}
MY_SECRET_KEY = 'khangdepzai'

cwd = os.getcwd()
UPLOAD_FOLDER = cwd + '/uploaded/'

app = Flask(__name__)

app.config['SECRET_KEY'] = MY_SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(file_name):
    return '.' in file_name and \
           file_name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', hostname=hostname)


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'myfile' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['myfile']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            global filename
            filename = str(datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S.csv"))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename)))

            return redirect(url_for('result'))

    return ''


@app.route('/result', methods=['GET'])
def result():
    uploaded_file = filename
    file_dir = cwd + '/uploaded/' + uploaded_file
    path = Path(file_dir)
    path.parent.mkdir(parents=True, exist_ok=True)

    content = []

    file_open = open(path, "r", encoding='utf-8')

    file_content = file_open.readlines()[1:]
    for line in file_content:
        refined_line = re.sub('[^0-9,]+', '', line)
        content_mini = refined_line.split(',')
        content.append(content_mini)

    return render_template('result.html', hostname=hostname, uploaded_file=uploaded_file, content=content)


if __name__ == '__main__':
    app.run(debug=True)
