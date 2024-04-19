import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/home/bolt/py/ID1110/froject/static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'secret_key'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/selection', methods = ['GET','POST'])
def selection():
    return render_template('selection.html')



@app.route('/upload', methods = ['GET', 'POST'])
def index(select = request.form.get('dropdown')):
    global model 
    model = select
    try:  
        return render_template('index.html', model = select)
    except:
        return 404

@app.route('/upload/display', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('download_file', name=filename))
            # print(file.filename)
            # return redirect("http://127.0.0.1:5000/success")
            return render_template('display.html', file_path=filename)

@app.route("/success")
def success():
    if model == "Pneumonia":
        return "Pneumonia"
    if model == "Brain Tumor":
        return "Brain Tumor"
    if model == "Melanoma":
        return "Melanoma"
    else:
        return 