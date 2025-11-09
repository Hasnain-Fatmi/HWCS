from joblib import load
from PIL import Image
import numpy as np
from skimage.feature import graycomatrix, graycoprops
import os

# Load models at startup
MODEL_PATH = "models/knn_model.joblib"
SCALER_PATH = "models/scaler.joblib"

try:
    model = load(MODEL_PATH)
    scaler = load(SCALER_PATH)
except Exception as e:
    print(f"Error loading models: {e}")
    model = None
    scaler = None


def extract_glcm_features(image_path):
    """Extract GLCM features from an image"""
    with Image.open(image_path) as image:
        grayscale_image = image.convert('L')
        grayscale_image_np = np.array(grayscale_image)
        glcm = graycomatrix(
            grayscale_image_np,
            [1],
            [0],
            256,
            symmetric=True,
            normed=True
        )
        contrast = graycoprops(glcm, 'contrast')[0, 0]
        dissimilarity = graycoprops(glcm, 'dissimilarity')[0, 0]
        homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]
        energy = graycoprops(glcm, 'energy')[0, 0]
        correlation = graycoprops(glcm, 'correlation')[0, 0]
        return [contrast, dissimilarity, homogeneity, energy, correlation]


def predict_handwriting(image_path):
    """Predict the writer of a handwriting sample"""
    if model is None or scaler is None:
        raise Exception("Models not loaded properly")

    # Extract features
    features = extract_glcm_features(image_path)

    # Scale features
    features_scaled = scaler.transform([features])

    # Make prediction
    prediction = model.predict(features_scaled)

    # Return the predicted writer (convert array to string)
    return prediction[0] if len(prediction) > 0 else "unknown"
