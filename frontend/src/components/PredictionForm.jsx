import React, { useState } from 'react';
import './PredictionForm.css';

const PredictionForm = ({ onPredict, loading }) => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      // Validate file type
      if (!file.type.startsWith('image/')) {
        alert('Please select an image file');
        return;
      }

      // Validate file size (max 10MB)
      if (file.size > 10 * 1024 * 1024) {
        alert('Image size must be less than 10MB');
        return;
      }

      setSelectedFile(file);
      
      // Create preview
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreview(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (selectedFile) {
      onPredict(selectedFile);
    }
  };

  const handleReset = () => {
    setSelectedFile(null);
    setPreview(null);
    document.getElementById('file-input').value = '';
  };

  return (
    <div className="prediction-form">
      <h2>Upload Vehicle Image</h2>
      <p className="form-description">
        Select an image of a vehicle to classify its category
      </p>
      
      <form onSubmit={handleSubmit}>
        <div className="file-input-container">
          <input
            type="file"
            accept="image/*"
            onChange={handleFileChange}
            disabled={loading}
            id="file-input"
          />
          <label htmlFor="file-input" className="file-label">
            {selectedFile ? '📷 Change Image' : '📁 Choose Image'}
          </label>
          {selectedFile && (
            <span className="file-name">{selectedFile.name}</span>
          )}
        </div>

        {preview && (
          <div className="preview-container">
            <img src={preview} alt="Preview" className="preview-image" />
          </div>
        )}

        <div className="button-group">
          <button 
            type="submit" 
            disabled={!selectedFile || loading}
            className="predict-button"
          >
            {loading ? '🔄 Predicting...' : '🚀 Predict Category'}
          </button>
          
          <button 
            type="button" 
            onClick={handleReset}
            disabled={loading || !selectedFile}
            className="reset-button"
          >
            🔁 Reset
          </button>
        </div>
      </form>
    </div>
  );
};

export default PredictionForm;
