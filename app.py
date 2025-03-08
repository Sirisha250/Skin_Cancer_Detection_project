from flask import Flask, request, render_template
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Load the saved Keras model
model = load_model('C:\\xampp\\htdocs\\skin_cancer_app\\model.h5')

# Define the image size your model expects
IMG_HEIGHT = 150  # Change to your model's input size
IMG_WIDTH = 150   # Change to your model's input size

# Function to preprocess the uploaded image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(IMG_HEIGHT, IMG_WIDTH))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize if you did this during training
    return img_array

@app.route('/')
def home():
    return render_template('index.html')  # Create this template

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file uploaded!', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file!', 400

    # Save the uploaded image temporarily
    img_path = os.path.join('uploads', file.filename)
    file.save(img_path)

    # Preprocess the image
    processed_image = preprocess_image(img_path)

    # Make prediction
    predictions = model.predict(processed_image)
    predicted_class = 'Malignant' if predictions[0] > 0.5 else 'Benign'  # Adjust threshold based on your model

    # Clean up the uploaded image file
    os.remove(img_path)

    return f'The model predicts: {predicted_class}'

if __name__ == '__main__':
    app.run(debug=True)
