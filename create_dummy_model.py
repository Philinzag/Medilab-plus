#!/usr/bin/env python3
"""
Quick model creator for deployment testing
Creates a minimal CNN model for skin disease classification
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import os

def create_dummy_model():
    """Create a simple CNN model for testing deployment"""
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dropout(0.5),
        Dense(512, activation='relu'),
        Dense(3, activation='softmax')  # 3 classes: Acne, Atopic Dermatitis, Scabies
    ])
    
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

if __name__ == "__main__":
    print("Creating dummy model for deployment testing...")
    
    # Create models directory
    os.makedirs('./models', exist_ok=True)
    
    # Create model
    model = create_dummy_model()
    
    # Save model
    model.save('./models/model.h5')
    print("✅ Model saved to ./models/model.h5")
    
    # Also save weights with correct filename format
    model.save_weights('./models/model.weights.h5')
    print("✅ Weights saved to ./models/model.weights.h5")
    
    print("\n📋 Model Summary:")
    model.summary()
    
    print("\n🚀 Ready for deployment!")
    print("Note: This is a dummy model for testing. Train with real data for production use.")
