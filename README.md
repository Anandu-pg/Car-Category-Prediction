# Vehicle Category Prediction

AI-powered application for automatic vehicle classification using Deep Learning with InceptionV3.

## About
This application classifies vehicles into 10 categories:
- SUV, Bus, Family Sedan, Fire Engine, Heavy Truck
- Jeep, Minibus, Racing Car, Taxi, Truck

## Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/Anandu-pg/Car-Category-Prediction.git
cd Car-Category-Prediction
```

### 2. Setup Environment
```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
cd frontend && npm install && cd ..
```

### 3. Run Application
```bash
python run.py
```

This will automatically:
- Start the backend server (http://localhost:8000)
- Launch the frontend (http://localhost:3000)
- Open your default browser

## Tech Stack
- Backend: FastAPI, TensorFlow
- Frontend: React
- Model: InceptionV3 (Transfer Learning)

## License
MIT License

Made with ❤️ using FastAPI, React, and TensorFlow