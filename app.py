import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory, send_file

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg',
                     'jpeg', 'mp4', 'mkv', 'mp3', 
                     'epub', 'hevc', 'mov', 'mpeg', 'srt', 'rar'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')

    if request.method == 'POST':
        # check if the post request has the file part
        file = request.files['file']
    
        if file.filename:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('downloads'))
        return redirect(url_for('downloads'))

@app.route("/downloads")
def downloads():
    thisdir = os.getcwd()
    print(os.path.join(thisdir, 'uploads'))
    files = os.listdir(os.path.join(thisdir, 'uploads'))
    files.remove(".gitignore")
    return render_template('downloads.html', files=files)

@app.route("/download_file/<name>")
def download_file(name):
    # return send_from_directory(app.config["UPLOAD_FOLDER"], name)
    thisdir = os.getcwd()
    file = os.path.join('uploads', name)
    return send_file(file, as_attachment=True)

@app.route("/delete_file/<name>")
def delete_file(name):
    # return send_from_directory(app.config["UPLOAD_FOLDER"], name)
    thisdir = os.getcwd()
    file = os.path.join('uploads', name)
    os.remove(file)
    return redirect(url_for('downloads'))
