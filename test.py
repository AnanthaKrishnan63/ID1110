import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from predictor import pneumonia, braintumor

UPLOAD_FOLDER = '/home/bolt/py/ID1110/froject/static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'secret_key'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def main():
    return redirect('/selection')

@app.route('/selection', methods = ['GET','POST'])
def selection():
    return render_template('selection1.html')



@app.route('/upload', methods = ['GET', 'POST'])
def index():
    select = request.form.get('dropdown')
    global model 
    model = select
    print("")
    print(model)
    print("")
    try:  
        return render_template('index1.html', model = select)
    except:
        return 404

@app.route('/upload/display', methods=['POST', 'GET'])
def upload_file():
    global filepath
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
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            print("")
            print(filepath)
            print("")
            return render_template('display.html', file_path=filename)

# Route for displaying the prediction result

@app.route("/success")
def success():
    if model == "Pneumonia":
        print("")
        print(pneumonia(filepath))
        print("")
        if pneumonia(filepath) < 0.5:
            return render_template('pneumonia.html', img = 'static/nopneumonia.jpg', message = "The patient probably doesn't have Pneumonia")
        if pneumonia(filepath)>= 0.5:
            return render_template('pneumonia.html', img = 'static/yespneumonia.jpeg', message = "The patient probably has Pneumonia")
    if model == "Brain Tumor":
        print("")
        print(braintumor(filepath))
        print("")
        if max(braintumor(filepath)[0]) == braintumor(filepath)[0][0]:
            return render_template('pneumonia.html', img = 'static/glioma.jpg', message = "The patient has a good chance of having Glioma Tumor.")
        if max(braintumor(filepath)[0]) == braintumor(filepath)[0][1]:
            return render_template('pneumonia.html', img = 'static/braintumor1.webp', message = "The patient has a good chance of having meningioma Tumor.")
        if max(braintumor(filepath)[0]) == braintumor(filepath)[0][2]:
            return render_template('pneumonia.html', img = 'static/nopneumonia.jpg', message = "The patient has a good chance of having no Tumor")
        if max(braintumor(filepath)[0]) == braintumor(filepath)[0][3]:
            return render_template('pneumonia.html', img = 'static/pitutary.jpg', message = "The patient has a good chance of having pituitary Tumor.")
    else:
        return "Error finding Model. Please try again"