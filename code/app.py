from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
from flask import Flask, render_template, request
from model import Fruit


app = Flask(__name__)
dropzone = Dropzone(app)
# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'
# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


@app.route('/', methods=['GET', 'POST'])
def index():
    # list to hold our uploaded image urls
    file_urls = []

    if request.method == 'POST':
        file_obj = request.files
        for f in file_obj:
            file = request.files.get(f)

            # save the file with to our photos folder
            filename = photos.save(
                file,
                name=file.filename
            )
            # append image urls
            file_urls.append(photos.url(filename))
            fruit = Fruit()
            path = "uploads/" + file.filename
            #print("Path : %s" % path)
            result = fruit.classify(path)
            result = result[0][0]
            f= open("result.txt","w+")
            f.write(result)
            f.close()
            os.remove(r'uploads/'+ filename)
        return "uploading..."
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/result')
def results():
    f= open("result.txt","r")
    result = f.read()
    f.close()
    return render_template('result.html',result=result)

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


app.run(host='0.0.0.0',port =5500,debug=True)
