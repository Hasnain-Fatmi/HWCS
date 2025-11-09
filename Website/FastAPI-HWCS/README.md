# HWCS - Handwriting Classification System (FastAPI)

> **Note:** This is a **proof-of-concept demonstration** project showcasing AI-powered handwriting analysis.

A modern, AI-powered handwriting classification system built with FastAPI. This demo system uses machine learning to identify handwriting from three specific writers (Hasnain, Mehdy, and Umair), demonstrating the potential of handwriting analysis technology.

## 🎯 Demo Purpose

This project is designed as a **portfolio demonstration** to showcase:
- Machine learning model deployment
- Modern web application development
- Full-stack implementation (ML + FastAPI + Frontend)
- Cloud deployment capabilities

**Current Scope:** The ML model is trained specifically on handwriting samples from three individuals and is not intended for general-purpose writer identification.

## Features

✨ **Modern UI Design**
- Beautiful gradient color scheme with purple theme
- Responsive design for all devices
- Smooth animations and transitions
- Interactive demo samples with click-to-analyze

🤖 **AI-Powered Classification**
- KNN-based writer identification
- GLCM (Gray Level Co-occurrence Matrix) feature extraction
- Pre-trained model on 3 specific writers
- Instant predictions on demo images

🚀 **Easy Deployment**
- Optimized for Vercel deployment
- Lightweight FastAPI backend
- Static file serving included
- 12 demo samples (4 per writer)

## Project Structure

```
FastAPI-HWCS/
├── main.py                 # FastAPI application
├── utils.py                # ML prediction utilities
├── requirements.txt        # Python dependencies
├── vercel.json            # Vercel configuration
├── templates/             # HTML templates
│   ├── home.html
│   └── result.html
├── static/                # Static assets
│   ├── css/
│   │   ├── home.css
│   │   └── result.css
│   ├── images/
│   └── demo_images/
├── models/                # ML models
│   ├── knn_model.joblib
│   └── scaler.joblib
└── uploads/               # Temporary upload storage

```

## Local Development

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Installation

1. Navigate to the project directory:
```bash
cd Website/FastAPI-HWCS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the development server:
```bash
python main.py
```

or

```bash
uvicorn main:app --reload
```

4. Open your browser and go to:
```
http://localhost:8000
```

## Deployment to Vercel

### Option 1: Using Vercel Dashboard (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Add FastAPI HWCS platform"
   git push origin main
   ```

2. **Import to Vercel**
   - Go to https://vercel.com
   - Click "Add New Project"
   - Import your GitHub repository
   - Set **Root Directory** to: `Website/FastAPI-HWCS`
   - Click "Deploy"

3. **Done!** Your app will be live at `https://your-app.vercel.app`

### Option 2: Using Vercel CLI

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Login to Vercel:
```bash
vercel login
```

3. Deploy:
```bash
cd Website/FastAPI-HWCS
vercel --prod
```

## API Endpoints

- `GET /` - Home page
- `POST /predict` - Upload and analyze handwriting
- `GET /health` - Health check endpoint

## Technology Stack

- **Backend**: FastAPI
- **ML**: scikit-learn, scikit-image
- **Image Processing**: Pillow, OpenCV
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Vercel

## Demo Images

The platform includes **12 interactive demo samples** from three writers:
- **Hasnain** - 4 samples
- **Mehdy** - 4 samples
- **Umair** - 4 samples

**Interactive Demo Feature:** Users can simply click on any demo image to instantly analyze it, no upload required! Each sample showcases different handwriting characteristics that the model uses for classification.

## Improvements Over Django Version

1. ✅ Lighter weight and faster
2. ✅ Easier Vercel deployment
3. ✅ No database required
4. ✅ Modern async/await support
5. ✅ Better static file handling
6. ✅ Simpler configuration

## Notes

- Uploaded images are temporarily stored and automatically deleted after prediction
- The system uses GLCM (Gray Level Co-occurrence Matrix) for feature extraction
- Model accuracy depends on image quality and handwriting style similarity
- **This is a demo system** trained on only 3 writers - not for production use

## Future Enhancements

This proof-of-concept can be expanded with:
- 📊 Training on larger datasets with more writers
- 🔬 Advanced feature extraction (deep learning-based)
- 📈 Confidence scores and probability distributions
- 🎨 Support for different languages and writing styles
- 💾 Database integration for storing analysis history
- 🔐 User authentication and personalized model training
- 📱 Mobile app development

## License

© 2024 HWCS. All rights reserved.

---

**Built by:** Hasnain, Mehdy, and Umair
**Purpose:** Academic project & portfolio demonstration
**Technology Stack:** Python, FastAPI, scikit-learn, JavaScript
