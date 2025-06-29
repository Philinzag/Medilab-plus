# Usage: python app.py
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.models import Sequential, load_model
import numpy as np
import argparse
import imutils
import cv2
import time
import uuid
import base64

img_width, img_height = 150, 150

# Use environment variables for paths with fallbacks
model_path = os.getenv('MODEL_PATH', './models/model.h5')
model_weights_path = os.getenv('MODEL_WEIGHTS_PATH', './models/weights.h5')

# Create uploads directory if it doesn't exist
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model with error handling
try:
    model = load_model(model_path)
    print(f"Model loaded successfully from {model_path}")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])


def get_as_base64(url):
    return base64.b64encode(request.get(url).content)


def predict(file):
    if model is None:
        return -1  # Error code for missing model
    
    try:
        x = load_img(file, target_size=(img_width, img_height))
        x = img_to_array(x)
        x = np.expand_dims(x, axis=0)
        array = model.predict(x)

        result = array[0]
        answer = np.argmax(result)
        if answer == 0:
            print("Label: Acne vulgaris")
        elif answer == 1:
            print("Label: Atopic Dermatitis")
        elif answer == 2:
            print("Label: Scabies ")
        return answer
    except Exception as e:
        print(f"Prediction error: {e}")
        return -1


def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4())  # Convert UUID format to a Python string.
    random = random.upper()  # Make all characters uppercase.
    random = random.replace("-", "")  # Remove the UUID '-'.
    return random[0:string_length]  # Return the random string.


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def template_test():
    return render_template('template.html', label='', sym='', treat='', imagesource='../uploads/skin-bn.jpg')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        import time
        start_time = time.time()
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            result = predict(file_path)
            
            # Handle prediction errors
            if result == -1:
                return render_template('template.html', 
                                     label='Error', 
                                     sym='Unable to process image. Please try again.',
                                     treat='Please upload a clear image and try again.',
                                     imagesource='../uploads/skin-bn.jpg')
        
            if result == 0:
                label = 'Acne vulgaris'
                sym = """Uninflamed blackheads to pus-filled pimples or large, red and tender bumps."""
                treat = """Prescription creams (eg: chemotherapy)
                or surgery(eg: electrosurgery) to remove the cancer."""
            elif result == 1:
                label = 'Atopic Dermatitis'
                sym = """Skin: rashes, dryness, flakiness, bumps, fissures, peeling, or redness."""
                treat = """Avoid the use of soap and other irritants. Certain creams or ointments may also provide relief from the itching."""
            elif result == 2:
                label = 'scabies'
                sym = """ Intense itching in the area where the mites burrow
                """
                treat = """Scabies can be treated by killing the mites and their eggs with medication that's applied from the neck down and left on for eight hours"""
            
          

            print(result)
            print(file_path)
            filename = my_random_string(6) + filename

            os.rename(file_path, os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("--- %s seconds ---" % str(time.time() - start_time))
            return render_template('template.html', label=label, sym=sym, treat=treat,
                                   imagesource='../uploads/' + filename)


from flask import send_from_directory


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


from werkzeug import SharedDataMiddleware

app.add_url_rule('/uploads/<filename>', 'uploaded_file',
                 build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads': app.config['UPLOAD_FOLDER']
})

if __name__ == "__main__":
    port = int(os.getenv('PORT', 3000))
    debug_mode = os.getenv('FLASK_ENV') != 'production'
    
    app.debug = debug_mode
    app.run(host='0.0.0.0', port=port)
