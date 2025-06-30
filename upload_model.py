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

def convert_drive_link(folder_link):
    """Convert Google Drive folder link to instructions for getting file IDs"""
    print("\n🔗 Converting Google Drive Link:")
    print(f"Folder Link: {folder_link}")
    print("\n📋 To get direct download links:")
    print("1. Open your folder link in browser")
    print("2. Right-click on model.h5 file")
    print("3. Select 'Get Link' or 'Copy Link'")
    print("4. Make sure it's set to 'Anyone with the link can view'")
    print("5. Copy the file-specific link (should contain the file ID)")
    print("6. Extract the FILE_ID from the URL")
    print("7. Use this format: https://drive.google.com/uc?id=FILE_ID&export=download")
    
    # Extract folder ID for reference
    if "folders/" in folder_link:
        folder_id = folder_link.split("folders/")[1].split("?")[0]
        print(f"\n📁 Your folder ID: {folder_id}")
        print("📝 Next step: Get the individual file ID for model.h5")

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
    
    # Convert the provided Google Drive link
    folder_link = "https://drive.google.com/drive/folders/1NHPA061HIArXB4rYAQJZK8c3XjPmHq_O?usp=sharing"
    convert_drive_link(folder_link)
    
    print("\n🚀 Once you have the direct download link:")
    print("1. Update the MODEL_DOWNLOAD_URL in build.sh")
    print("2. Push changes to GitHub")
    print("3. Render will automatically redeploy with your trained model!")
