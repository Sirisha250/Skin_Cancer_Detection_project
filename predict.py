import sys
import cv2
import keras
import numpy as np

# Check if an image path was provided
if len(sys.argv) < 2:
    print("No image path provided")
    sys.exit()

img_path = sys.argv[1]
print(f"Processing image: {img_path}")

# Load and preprocess the image
image = cv2.imread(img_path)
if image is None:
    print("Error loading image.")
    sys.exit()

# Preprocess the image (resize, normalize, etc.)
image = cv2.resize(image, (150, 150))  # Adjust size based on your model
image = image / 255.0  # Normalize if required

# Make prediction using your model
model = keras.models.load_model("C:\\xampp\\htdocs\\skin_cancer_app\\best_model.keras")  # Adjust path as needed
prediction = model.predict(image.reshape(1, 150, 150, 3))  # Adjust shape if needed

# Interpretation of prediction
prediction_value = prediction[0][0]  # Get the prediction value

# Define thresholds for cancerous vs. non-cancerous and risk levels
threshold = 0.5  # Base threshold for possibly cancerous
high_risk_threshold = 0.9  # High confidence threshold
moderate_risk_threshold = 0.7  # Moderate confidence threshold

# Predict cancer type and provide advice based on risk level
if prediction_value < threshold:
    print(f"Prediction: Non-cancerous (Confidence: {1 - prediction_value:.2f})")
    print("Advice: Lower risk. Maintain routine skin checks and monitor any changes.")
elif threshold <= prediction_value < moderate_risk_threshold:
    print(f"Prediction: Possibly Cancerous - Further testing recommended (Confidence: {prediction_value:.2f})")
    print("Advice: Moderate risk. Schedule a follow-up with a dermatologist to confirm diagnosis.")
elif moderate_risk_threshold <= prediction_value < high_risk_threshold:
    cancer_type = "Squamous Cell Carcinoma"
    print(f"Prediction: Cancerous (Confidence: {prediction_value:.2f}), Type: {cancer_type}")
    print("Advice: Moderate risk. Promptly consult a dermatologist for treatment options.")
elif prediction_value >= high_risk_threshold:
    cancer_type = "Melanoma"
    print(f"Prediction: Cancerous (Confidence: {prediction_value:.2f}), Type: {cancer_type}")
    print("Advice: High risk. Immediate medical attention is recommended due to higher malignancy risk.")
