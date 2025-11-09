from joblib import load
from PIL import Image
import numpy as np
from skimage.feature import graycomatrix, graycoprops, local_binary_pattern
from scipy import ndimage
from scipy.stats import skew, kurtosis
import os
import warnings

# Model file paths
MODEL_PATH = "models/k_nearest_neighbors_model.joblib"
SCALER_PATH = "models/scaler_improved.joblib"
LABEL_ENCODER_PATH = "models/label_encoder.joblib"

try:
    model = load(MODEL_PATH)
    scaler = load(SCALER_PATH)
    label_encoder = load(LABEL_ENCODER_PATH)
    print(f"[OK] Models loaded successfully")
except Exception as e:
    print(f"[ERROR] Failed to load models: {e}")
    print(f"Attempted paths:")
    print(f"  Model: {MODEL_PATH}")
    print(f"  Scaler: {SCALER_PATH}")
    print(f"  Label Encoder: {LABEL_ENCODER_PATH}")
    model = None
    scaler = None
    label_encoder = None


class EnhancedFeatureExtractor:
    """Extracts an expanded set of features from a grayscale image array or image path.

    Features included:
    - GLCM (contrast, dissimilarity, homogeneity, energy, correlation) for 4 angles
    - LBP (mean)
    - Statistical features: mean, std, skew, kurtosis
    - Edge features: mean edge magnitude and edge density
    """

    def extract_glcm_features(self, image_array):
        features = []
        angles = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]
        for angle in angles:
            glcm = graycomatrix(image_array, distances=[1], angles=[angle],
                                levels=256, symmetric=True, normed=True)
            features.append(float(graycoprops(glcm, 'contrast')[0, 0]))
            features.append(float(graycoprops(glcm, 'dissimilarity')[0, 0]))
            features.append(float(graycoprops(glcm, 'homogeneity')[0, 0]))
            features.append(float(graycoprops(glcm, 'energy')[0, 0]))
            features.append(float(graycoprops(glcm, 'correlation')[0, 0]))
        return features

    def extract_lbp_features(self, image_array):
        radius = 1
        n_points = 8 * radius
        lbp = local_binary_pattern(image_array, n_points, radius, method='uniform')
        return [float(np.mean(lbp))]

    def extract_statistical_features(self, image_array):
        features = []
        features.append(float(np.mean(image_array)))
        features.append(float(np.std(image_array)))
        # flatten for skew/kurtosis
        flat = image_array.flatten()
        # handle constant arrays which can cause warnings
        try:
            features.append(float(skew(flat)))
        except Exception:
            features.append(0.0)
        try:
            features.append(float(kurtosis(flat)))
        except Exception:
            features.append(0.0)

        sx = ndimage.sobel(image_array, axis=0, mode='constant')
        sy = ndimage.sobel(image_array, axis=1, mode='constant')
        edge_magnitude = np.hypot(sx, sy)
        # edge density: proportion of pixels above mean edge magnitude
        mean_edge = float(np.mean(edge_magnitude))
        edge_density = float(np.sum(edge_magnitude > mean_edge) / edge_magnitude.size)
        features.append(edge_density)
        features.append(mean_edge)
        return features

    def extract_all_features(self, image_path_or_array):
        """Accepts an image path or a numpy array (grayscale) and returns feature list or None on error."""
        try:
            if isinstance(image_path_or_array, (str, os.PathLike)):
                with Image.open(image_path_or_array) as image:
                    grayscale_image = image.convert('L')
                    image_array = np.array(grayscale_image)
            else:
                # assume already a numpy array / PIL Image
                if hasattr(image_path_or_array, 'convert'):
                    grayscale_image = image_path_or_array.convert('L')
                    image_array = np.array(grayscale_image)
                else:
                    image_array = np.array(image_path_or_array)

            # ensure dtype is uint8-like range for GLCM levels
            if image_array.max() > 255 or image_array.min() < 0:
                # scale/clamp to 0-255
                image_array = np.clip(image_array, 0, 255).astype(np.uint8)

            glcm_features = self.extract_glcm_features(image_array)
            lbp_features = self.extract_lbp_features(image_array)
            stat_features = self.extract_statistical_features(image_array)
            return glcm_features + lbp_features + stat_features
        except Exception as e:
            warnings.warn(f"Error extracting features: {e}")
            return None


def predict_handwriting(image_path_or_array):
    """Predict the writer for a given image path or image-like object.

    Returns the predicted label (string) or raises an informative exception.
    """
    if model is None or scaler is None or label_encoder is None:
        raise RuntimeError("Models not loaded properly")

    extractor = EnhancedFeatureExtractor()
    features = extractor.extract_all_features(image_path_or_array)
    if features is None:
        raise ValueError("Could not extract features from input image")

    # Ensure correct shape
    features_arr = np.array([features])
    try:
        features_scaled = scaler.transform(features_arr)
    except Exception as e:
        raise RuntimeError(f"Feature scaling failed: {e}")

    try:
        prediction = model.predict(features_scaled)
    except Exception as e:
        raise RuntimeError(f"Model prediction failed: {e}")

    # Convert numeric prediction to string label
    if len(prediction) > 0:
        try:
            # prediction[0] is a numpy int, convert to actual class name
            predicted_label = label_encoder.inverse_transform([prediction[0]])[0]
            return str(predicted_label)
        except Exception as e:
            # Fallback to numeric prediction if label encoder fails
            return str(prediction[0])
    
    return "unknown"
