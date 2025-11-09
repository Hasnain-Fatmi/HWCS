# HWCS - Handwriting Classification System

AI-powered writer identification system built with FastAPI and scikit-learn.

## 🚀 Live Demo

[Click here to view the live demo](https://your-app.onrender.com)

## 📋 Features

- **AI-Powered Classification**: Identifies handwriting samples from three writers (Hasnain, Mehdy, Umair)
- **Advanced Feature Extraction**: Uses GLCM, LBP, and statistical features (27 features total)
- **Interactive Demo**: Try pre-loaded samples or upload your own
- **Fast API**: Built with FastAPI for high performance
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Technology Stack

- **Backend**: FastAPI, Python 3.11
- **ML Model**: K-Nearest Neighbors (scikit-learn)
- **Feature Extraction**: scikit-image, scipy
- **Image Processing**: Pillow, OpenCV
- **Deployment**: Render

## 📊 Model Details

- **Algorithm**: K-Nearest Neighbors with Manhattan distance
- **Features**: 27 enhanced features
  - GLCM features (20): texture analysis across 4 angles
  - LBP features (1): local binary patterns
  - Statistical features (6): mean, std, skew, kurtosis, edge density, edge magnitude
- **Training Dataset**: [View on GitHub](https://github.com/Hasnain-Fatmi/HWCS/tree/main/orignal_images)

## 🏃 Local Development

### Prerequisites

- Python 3.11+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Hasnain-Fatmi/HWCS.git
cd HWCS/Website/FastAPI-HWCS

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn main:app --reload
```

Visit `http://localhost:8000` in your browser.

## 🚀 Deployment on Render

This app is configured for easy deployment on Render:

1. Fork/clone this repository
2. Sign up at [render.com](https://render.com)
3. Create a new "Web Service"
4. Connect your GitHub repository
5. Render will auto-detect the `render.yaml` configuration
6. Click "Deploy"

The app will be live at `https://your-app.onrender.com`

## 📁 Project Structure

```
FastAPI-HWCS/
├── main.py                 # FastAPI application
├── utils.py                # Feature extraction & prediction logic
├── requirements.txt        # Python dependencies
├── render.yaml            # Render deployment config
├── models/                # ML models
│   ├── k_nearest_neighbors_model.joblib
│   ├── scaler_improved.joblib
│   └── label_encoder.joblib
├── static/                # CSS, images, demo samples
│   ├── css/
│   ├── images/
│   └── demo_images/
└── templates/             # HTML templates
    ├── home.html
    └── result.html
```

## 🔍 API Endpoints

- `GET /` - Home page with upload form
- `POST /predict` - Predict writer from uploaded image
- `POST /predict-demo` - Predict writer from demo image
- `GET /health` - Health check endpoint

## 👥 Authors

- Hasnain Fatmi
- Mehdy
- Umair

## 📝 License

This project is part of an academic portfolio demonstrating machine learning and web development skills.

## 🔗 Links

- [GitHub Repository](https://github.com/Hasnain-Fatmi/HWCS)
- [Training Dataset](https://github.com/Hasnain-Fatmi/HWCS/tree/main/orignal_images)
- [Live Demo](https://your-app.onrender.com)

---

**Note**: This is a proof-of-concept demo trained on a specific dataset. For production use with different writers, the model would need to be retrained.
