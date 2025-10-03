from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Vehicle Classification API"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    
    # Model settings
    MODEL_PATH: str = "app/models/vehicle_classification_model.h5"
    CLASS_INDICES_PATH: str = "app/models/class_indices.json"
    IMAGE_SIZE: tuple = (224, 224)
    
    # CORS settings
    ALLOWED_ORIGINS: list = ["http://localhost:3000", "http://localhost:5173"]

settings = Settings()
