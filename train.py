import tensorflow as tf

print("✅ TensorFlow version:", tf.__version__)  # Debugging print

import os
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers # type: ignore
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
from tensorflow.keras.callbacks import ModelCheckpoint # type: ignore

print("✅ All imports loaded successfully!")  # Debugging print

# Define paths
train_dir = r'C:\xampp\htdocs\skin_cancer_app\HAM10000_images_part_1'
validation_dir = r'C:\xampp\htdocs\skin_cancer_app\HAM10000_images_part_2'

print("✅ Training directory:", train_dir)
print("✅ Validation directory:", validation_dir)

# Check if the directories exist
if not os.path.exists(train_dir):
    print("❌ Training directory does not exist!")
if not os.path.exists(validation_dir):
    print("❌ Validation directory does not exist!")

# Data preprocessing
train_datagen = ImageDataGenerator(rescale=1.0/255)
validation_datagen = ImageDataGenerator(rescale=1.0/255)

print("✅ Data generators initialized.")

# Load training data
try:
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary'
    )
    print("✅ Training data loaded successfully!")
except Exception as e:
    print("❌ Error loading training data:", e)

# Load validation data
try:
    validation_generator = validation_datagen.flow_from_directory(
        validation_dir,
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary'
    )
    print("✅ Validation data loaded successfully!")
except Exception as e:
    print("❌ Error loading validation data:", e)

# Build the model
print("✅ Building model...")
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

print("✅ Model built successfully!")

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print("✅ Model compiled successfully!")

# Checkpoint
save_path = r'C:\xampp\htdocs\skin_cancer_app'
checkpoint = ModelCheckpoint(
    os.path.join(save_path, 'best_model.keras'),
    monitor='val_accuracy',
    save_best_only=True,
    mode='max'
)
print("✅ Checkpoint initialized.")

# Start Training
print("🚀 Starting model training...")
try:
    model.fit(train_generator, validation_data=validation_generator, epochs=10, callbacks=[checkpoint])
    print("✅ Training completed!")
except Exception as e:
    print("❌ Error during training:", e)

# Save final model
try:
    model.save(os.path.join(save_path, 'model.keras'))
    print("✅ Final model saved successfully!")
except Exception as e:
    print("❌ Error saving final model:", e)
print(tf.__version__)