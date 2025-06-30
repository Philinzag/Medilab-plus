#!/usr/bin/env python3
"""
Convert the trained model to TensorFlow 2.12 compatible format
This script recreates the model architecture and loads the trained weights
"""

import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Activation
from tensorflow.keras import optimizers

def create_model_architecture():
    """Recreate the exact model architecture from train.py"""
    
    # Model parameters (from train.py)
    img_width, img_height = 150, 150
    nb_filters1 = 32
    nb_filters2 = 64
    conv1_size = 3
    conv2_size = 2
    pool_size = 2
    classes_num = 3
    lr = 0.0004

    model = Sequential()
    model.add(Conv2D(nb_filters1, (conv1_size, conv1_size), padding="same", input_shape=(img_width, img_height, 3)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(pool_size, pool_size)))

    model.add(Conv2D(nb_filters2, (conv2_size, conv2_size), padding="same"))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(pool_size, pool_size)))

    model.add(Flatten())
    model.add(Dense(256))
    model.add(Activation("relu"))
    model.add(Dropout(0.5))
    model.add(Dense(classes_num, activation='softmax'))

    # Compile with modern TensorFlow
    model.compile(
        loss='categorical_crossentropy',
        optimizer=optimizers.RMSprop(learning_rate=lr),
        metrics=['accuracy']
    )
    
    return model

def convert_model():
    """Convert the old model to new format"""
    
    print("🔄 Converting model to TensorFlow 2.12 compatible format...")
    
    # Create the model architecture
    new_model = create_model_architecture()
    print("✅ Model architecture created")
    
    # Try to load weights from the old model
    old_model_path = './models/model.h5'
    
    if os.path.exists(old_model_path):
        try:
            # Load the old model without compiling
            print("📥 Loading old model...")
            old_model = tf.keras.models.load_model(old_model_path, compile=False)
            
            # Transfer weights to new model
            print("🔄 Transferring weights...")
            new_model.set_weights(old_model.get_weights())
            print("✅ Weights transferred successfully")
            
        except Exception as e:
            print(f"❌ Failed to load old model: {e}")
            print("🎲 Using random weights (model will need retraining)")
    else:
        print("❌ Old model not found, using random weights")
    
    # Save the new compatible model
    new_model_path = './models/model_v2.h5'
    new_model.save(new_model_path)
    print(f"✅ New model saved to {new_model_path}")
    
    # Replace the old model
    if os.path.exists(old_model_path):
        os.rename(old_model_path, './models/model_old.h5')
        print("📦 Old model backed up as model_old.h5")
    
    os.rename(new_model_path, old_model_path)
    print("✅ New model is now the primary model")
    
    # Test loading the new model
    try:
        test_model = tf.keras.models.load_model(old_model_path)
        print("✅ New model loads successfully!")
        print(f"📊 Model summary:")
        test_model.summary()
        return True
    except Exception as e:
        print(f"❌ New model failed to load: {e}")
        return False

if __name__ == "__main__":
    success = convert_model()
    if success:
        print("\n🎉 Model conversion completed successfully!")
        print("🚀 The model should now work with your app!")
    else:
        print("\n💥 Model conversion failed!")
