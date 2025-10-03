from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.predictor import classifier
from app.schemas.prediction import PredictionResponse, HealthResponse

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict_vehicle(file: UploadFile = File(...)):
    """
    Predict vehicle category from uploaded image
    
    Args:
        file: Image file uploaded by user
        
    Returns:
        Prediction results with confidence scores
    """
    # Validate file type
    if not file.content_type or not file.content_type.startswith('image/'):
        raise HTTPException(
            status_code=400, 
            detail="File must be an image (JPEG, PNG, etc.)"
        )
    
    try:
        # Read image bytes
        image_bytes = await file.read()
        
        # Validate file size (max 10MB)
        if len(image_bytes) > 10 * 1024 * 1024:
            raise HTTPException(status_code=400, detail="Image size must be less than 10MB")
        
        # Make prediction
        result = classifier.predict(image_bytes)
        
        return PredictionResponse(**result)
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Prediction failed: {str(e)}"
        )

@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Check if API is running"""
    return HealthResponse(
        status="healthy",
        message="Vehicle Classification API is running"
    )

@router.get("/classes")
async def get_classes():
    """Get all vehicle classes supported by the model"""
    return {
        "classes": list(classifier.class_indices.keys()),
        "total": len(classifier.class_indices)
    }
