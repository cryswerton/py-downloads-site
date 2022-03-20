import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/upload")
def upload():
    return render_template('upload.html')

@app.route("/downloads")
def downloads():
    thisdir = os.getcwd()
    print(os.path.join(thisdir, 'uploads'))
    files = os.listdir(os.path.join(thisdir, 'uploads'))
    return render_template('downloads.html', files=files)