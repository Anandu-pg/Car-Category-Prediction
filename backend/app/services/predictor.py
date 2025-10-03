import numpy as np
import json
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import io
from app.core.config import settings

class VehicleClassifier:
    """Vehicle classification model wrapper"""
    
    def __init__(self):
        """Load the trained model and class indices"""
        print("Loading model...")
        self.model = load_model(settings.MODEL_PATH)
        
        print("Loading class indices...")
        with open(settings.CLASS_INDICES_PATH, 'r') as f:
            self.class_indices = json.load(f)
        
        # Create reverse mapping: index -> class name
        self.index_to_class = {v: k for k, v in self.class_indices.items()}
        print("Model loaded successfully!")
    
    def preprocess_image(self, image_bytes: bytes):
        """
        Preprocess image for model prediction
        
        Args:
            image_bytes: Raw image bytes
            
        Returns:
            Preprocessed image array
        """
        # Open image from bytes
        img = Image.open(io.BytesIO(image_bytes))
        
        # Convert to RGB (in case of RGBA or grayscale)
        img = img.convert('RGB')
        
        # Resize to model input size
        img = img.resize(settings.IMAGE_SIZE)
        
        # Convert to array
        img_array = image.img_to_array(img)
        
        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)
        
        # Normalize pixel values to [0, 1]
        img_array = img_array / 255.0
        
        return img_array
    
    def predict(self, image_bytes: bytes) -> dict:
        """
        Make prediction on uploaded image
        
        Args:
            image_bytes: Raw image bytes
            
        Returns:
            Dictionary with prediction results
        """
        # Preprocess image
        processed_image = self.preprocess_image(image_bytes)
        
        # Make prediction
        predictions = self.model.predict(processed_image, verbose=0)[0]
        
        # Get predicted class
        predicted_idx = np.argmax(predictions)
        predicted_class = self.index_to_class[predicted_idx]
        confidence = float(predictions[predicted_idx])
        
        # Get all predictions as dictionary
        all_predictions = {
            self.index_to_class[i]: float(predictions[i])
            for i in range(len(predictions))
        }
        
        return {
            "predicted_class": predicted_class,
            "confidence": confidence,
            "all_predictions": all_predictions
        }

# Create a singleton instance
classifier = VehicleClassifier()
