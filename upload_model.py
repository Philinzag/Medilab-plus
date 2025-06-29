#!/usr/bin/env python3
"""
Upload trained model to cloud storage for deployment
Since GitHub has file size limits, we'll provide instructions for cloud storage
"""

import os

def get_file_size(filepath):
    """Get file size in MB"""
    size_bytes = os.path.getsize(filepath)
    size_mb = size_bytes / (1024 * 1024)
    return size_mb

if __name__ == "__main__":
    model_file = './models/model.h5'
    weights_file = './models/model.weights.h5'
    
    print("📊 Model File Sizes:")
    if os.path.exists(model_file):
        size = get_file_size(model_file)
        print(f"├── model.h5: {size:.2f} MB")
    
    if os.path.exists(weights_file):
        size = get_file_size(weights_file)
        print(f"└── model.weights.h5: {size:.2f} MB")
    
    print("\n🚫 GitHub Limitation:")
    print("GitHub has a 100MB file size limit, but our trained model is 171MB.")
    print("\n💡 Solutions:")
    print("1. Use Google Drive to host the model")
    print("2. Use Dropbox public links")
    print("3. Use Hugging Face Model Hub (recommended)")
    print("4. Use Git LFS (Large File Storage)")
    
    print("\n📝 Recommended Steps:")
    print("1. Upload model.h5 to Google Drive")
    print("2. Get a direct download link")
    print("3. Update build.sh to download during deployment")
    print("4. This keeps the repo lightweight while enabling deployment")
    
    print("\n🔗 Google Drive Upload Instructions:")
    print("1. Go to drive.google.com")
    print("2. Upload models/model.h5")
    print("3. Right-click → Share → Get Link")
    print("4. Change permissions to 'Anyone with the link'")
    print("5. Copy the file ID from the URL")
    print("6. Use format: https://drive.google.com/uc?id=FILE_ID&export=download")
