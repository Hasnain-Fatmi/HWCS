# Hugging Face Spaces Deployment Guide

## 🚀 Deploy to Hugging Face Spaces

### Step 1: Create a Space

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click **"Create new Space"**
3. Fill in details:
   - **Space name**: `hwcs-handwriting-classifier`
   - **License**: MIT
   - **SDK**: **Docker** ⚠️ Important!
   - **Visibility**: Public
4. Click **"Create Space"**

### Step 2: Upload Files

You have two options:

#### Option A: Git (Recommended)

```bash
# Navigate to your FastAPI-HWCS directory
cd d:\Github\HWCS\Website\FastAPI-HWCS

# Add Hugging Face remote (replace YOUR_USERNAME)
git init
git remote add hf https://huggingface.co/spaces/YOUR_USERNAME/hwcs-handwriting-classifier

# Add all files
git add .
git commit -m "Initial deployment to Hugging Face Spaces"

# Push to Hugging Face
git push hf main
```

#### Option B: Web Upload

1. In your Space page, click **"Files and versions"**
2. Click **"Add file"** → **"Upload files"**
3. Upload these files/folders:
   - `Dockerfile`
   - `main.py`
   - `utils.py`
   - `requirements.txt`
   - `models/` (all 3 .joblib files)
   - `static/` (entire folder)
   - `templates/` (entire folder)
   - `README_HF.md` (rename to `README.md` when uploading)

### Step 3: Wait for Build

- Hugging Face will automatically build your Docker container
- Check the **"Building"** status at the top
- Build takes ~5-10 minutes
- When complete, status changes to **"Running"** ✅

### Step 4: Access Your App

- Your app will be live at: `https://huggingface.co/spaces/YOUR_USERNAME/hwcs-handwriting-classifier`
- The interface will embed your FastAPI app
- Test with demo samples!

## 📋 Files Checklist

Make sure these files are uploaded:

- [x] `Dockerfile` - Container configuration
- [x] `main.py` - FastAPI application
- [x] `utils.py` - ML logic
- [x] `requirements.txt` - Python dependencies
- [x] `models/knn_model.joblib` - ML model
- [x] `models/scaler.joblib` - Feature scaler
- [x] `static/` - CSS, images, demos
- [x] `templates/` - HTML files
- [x] `README.md` - Space description

## 🔧 Troubleshooting

**Build fails?**
- Check logs in the Space page
- Ensure all model files are uploaded
- Verify Dockerfile syntax

**App not loading?**
- Make sure port 7860 is used (Hugging Face requirement)
- Check that SDK is set to "Docker"

**Slow predictions?**
- Free tier has CPU only
- First prediction may take longer

## ✨ Benefits of Hugging Face Spaces

- ✅ **100% Free** - No credit card needed
- ✅ **Always On** - No cold starts
- ✅ **ML Optimized** - Built for AI/ML demos
- ✅ **Great for Portfolio** - Showcases your ML work
- ✅ **Community** - Get discovered by ML practitioners

## 🔗 After Deployment

Add to your portfolio/resume:
```
🔗 Live Demo: https://huggingface.co/spaces/YOUR_USERNAME/hwcs-handwriting-classifier
```

---

**Need help?** Check Hugging Face Spaces documentation: https://huggingface.co/docs/hub/spaces
