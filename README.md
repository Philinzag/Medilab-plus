# Medilab-plus

## Overview
Medilab-plus is a web application that uses machine learning to diagnose skin diseases from uploaded images. The application can currently classify three types of skin conditions:
- Acne Vulgaris
- Atopic Dermatitis
- Scabies

## Features
- Real-time skin disease classification from uploaded images
- Provides symptoms and treatment information for diagnosed conditions
- User-friendly web interface

## Technology Stack
- **Backend**: Flask (Python)
- **Machine Learning**: Keras with TensorFlow
- **Frontend**: HTML, CSS, Bootstrap
- **Image Processing**: OpenCV

## Project Structure
- `app.py`: Main Flask application
- `train.py`: Script for training the CNN model
- `predic.py`: Script for making predictions
- `data/`: Directory containing training and validation datasets
- `models/`: Directory for storing trained models
- `static/`: Static assets (CSS, JS, images)
- `templates/`: HTML templates
- `uploads/`: Directory for uploaded images

## Model Architecture
The project uses a Convolutional Neural Network (CNN) with:
- 2 convolutional layers
- Max pooling layers
- Dropout for regularization
- Softmax activation for multiclass classification

## Installation and Setup

### Prerequisites
- Python 3.6+ (Python 3.7 recommended for 2019 compatibility)
- pip package manager

### Option 1: Quick Setup (2019 Compatible)
1. Clone the repository:
```bash
git clone https://github.com/yourusername/Medilab-plus.git
cd Medilab-plus
```

2. Install 2019 compatible dependencies:
```bash
pip install -r requirements-2019.txt
```

3. Run the application:
```bash
python app.py
```

4. Access the application at http://127.0.0.1:3000

### Option 2: Modern Setup (Updated Dependencies)
For production deployment with better security:

1. Install updated dependencies:
```bash
pip install -r requirements-deploy.txt
```

2. Copy environment file:
```bash
cp .env.example .env
```

3. Run the application:
```bash
python app.py
```

## Deployment

### Free Cloud Deployment (Render - Recommended)
The project is ready for deployment on Render's free tier:

1. Push your code to GitHub
2. Connect to [Render.com](https://render.com)
3. Use the included `render.yaml` and `build.sh` files
4. See `DEPLOYMENT.md` for detailed instructions

**Live Demo**: Once deployed, your app will be available at `https://your-app-name.onrender.com`

### Other Deployment Options
- **Railway**: $5 free credit monthly
- **PythonAnywhere**: Free tier for Python apps
- **Heroku**: Requires payment (free tier discontinued)

### Important Notes
- **2019 Compatibility**: Use `requirements-2019.txt` for immediate setup without code changes
- **Modern Versions**: Use `requirements-modern.txt` for latest features but requires code migration
- **Security**: 2019 versions may have known vulnerabilities; consider modern versions for production
- **Models**: Pre-trained models from 2019 should work with both setups

## Requirements Files
- `requirements.txt` - Default 2019 compatible versions
- `requirements-2019.txt` - Explicit 2019 versions with exact version numbers
- `requirements-modern.txt` - Latest compatible versions (requires code changes)
- `MIGRATION.md` - Guide for upgrading to modern versions

## Training New Models
To train a new model:
```bash
python train.py
```

Add the `-d` or `--development` flag for a quick test with fewer epochs:
```bash
python train.py -d
```

