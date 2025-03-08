from flask import Flask, request, render_template
from tensorflow import keras
from tensorflow.keras.preprocessing import image # type: ignore
import numpy as np

appy = Flask(__name__)

# Load the model
#model = keras.models.load_model('C:\xampp\htdocs\skin_cancer_app\best_model.keras')
model = keras.models.load_model('C:\\xampp\\htdocs\\skin_cancer_app\\best_model.keras')


@appy.route('/')
def home():
    return render_template('index.html')

@appy.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image']
        img = image.load_img(file, target_size=(150, 150))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)
        result = 'Malignant' if prediction[0] > 0.5 else 'Benign'

        return render_template('demo.html', prediction=result)

if __name__ == '__main__':
    appy.run(debug=False)
