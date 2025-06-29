# Deployment Guide for Medilab-plus

## Deploying to Render

### Prerequisites
1. Your trained model file should be in `./models/model.h5`
2. GitHub repository with your code

### Step 1: Prepare Your Repository
1. Ensure all files are committed to your GitHub repository
2. Make sure the `models/` directory contains your trained model
3. The deployment files are already created in your project

### Step 2: Deploy to Render
1. Go to [render.com](https://render.com) and sign up/login
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: medilab-plus (or your preferred name)
   - **Environment**: Python 3
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120`
   - **Plan**: Free

### Step 3: Environment Variables
In Render dashboard, add these environment variables:
- `FLASK_ENV` = `production`
- `PYTHON_VERSION` = `3.9.16`

### Step 4: Deploy
1. Click "Create Web Service"
2. Render will automatically build and deploy your app
3. The build process will take 5-10 minutes (TensorFlow is large)
4. Once deployed, you'll get a URL like: `https://medilab-plus.onrender.com`

### Important Notes

#### Model Considerations
- **Model Size**: If your model is large (>100MB), consider:
  - Using TensorFlow Lite for smaller models
  - Storing models in cloud storage (Google Drive, Dropbox) and downloading during build
  - Model compression techniques

#### Free Tier Limitations
- **Sleep Mode**: App sleeps after 15 minutes of inactivity
- **Build Time**: 500 build minutes/month
- **Bandwidth**: Limited but usually sufficient for personal projects

#### Performance Tips
- First request after sleep takes 30-60 seconds to wake up
- Consider upgrading to paid plan for production use
- Model predictions may take 5-15 seconds on free tier

### Alternative: Using Cloud Storage for Models

If your model is too large, you can store it on Google Drive and download it during deployment:

1. Upload your model to Google Drive and get a direct download link
2. Update `build.sh` to download the model:
   ```bash
   # Download model from Google Drive
   wget -O models/model.h5 "YOUR_GOOGLE_DRIVE_DIRECT_LINK"
   ```

### Troubleshooting

#### Build Fails
- Check build logs in Render dashboard
- Ensure all dependencies are in requirements-deploy.txt
- Verify model files exist

#### App Crashes
- Check application logs in Render dashboard
- Verify environment variables are set correctly
- Ensure model file is accessible

#### Slow Performance
- First request after sleep is always slow
- Consider model optimization
- Upgrade to paid plan for better performance

### Testing Your Deployment
1. Visit your Render URL
2. Upload a skin image
3. Verify the classification works
4. Check that all static assets load correctly

### Domain Configuration (Optional)
- You can add a custom domain in Render dashboard
- Free tier includes HTTPS automatically
