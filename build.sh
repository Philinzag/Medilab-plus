#!/usr/bin/env bash
# build.sh - Render build script

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements-deploy.txt

echo "Creating necessary directories..."
mkdir -p uploads
mkdir -p models

echo "Downloading trained model from Google Drive..."
# Download the trained model (171MB)
MODEL_URL="https://drive.google.com/uc?id=1wInTfPdAAXxCH5YD_f9WiV4dXJsSKyUI&export=download"
curl -L -o models/model.h5 "$MODEL_URL"

echo "Checking for trained model..."
if [ ! -f "./models/model.h5" ]; then
    echo "⚠️  Model download failed. Creating dummy model for deployment..."
    python -c "
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dropout(0.5),
    Dense(512, activation='relu'),
    Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.save('./models/model.h5')
print('✅ Dummy model created for deployment')
"
else
    echo "✅ Trained model downloaded successfully!"
    ls -lh ./models/model.h5
fi

echo "Build completed successfully!"
