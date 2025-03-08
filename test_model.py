import os
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define paths
test_dir = r'C:\xampp\htdocs\skin_cancer_app\HAM10000_images_part_2'  # Set this to your test data path

# Data preprocessing for test data
test_datagen = ImageDataGenerator(rescale=1.0/255)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(150, 150),  # Same as training data
    batch_size=32,
    class_mode='binary'  # Use 'categorical' for multi-class classification
)

# Load the saved model
model_path = os.path.join(r'C:\xampp\htdocs\skin_cancer_app', 'best_model.keras')
 # Change as necessary
model = keras.models.load_model(model_path)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(test_generator)
print(f'Test accuracy: {test_accuracy * 100:.2f}%')
print(f'Test loss: {test_loss:.4f}')
