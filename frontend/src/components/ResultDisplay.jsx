import React from 'react';
import './ResultDisplay.css';

const ResultDisplay = ({ result }) => {
  if (!result) return null;

  // Sort predictions by confidence (descending)
  const sortedPredictions = Object.entries(result.all_predictions)
    .sort(([, a], [, b]) => b - a)
    .slice(0, 5); // Show top 5 predictions

  return (
    <div className="result-display">
      <h2>Prediction Results</h2>
      
      <div className="main-prediction">
        <h3>Predicted Vehicle Type</h3>
        <div className="predicted-class">
          {result.predicted_class.replace(/_/g, ' ').toUpperCase()}
        </div>
        <div className="confidence">
          Confidence: {(result.confidence * 100).toFixed(2)}%
        </div>
        <div className="confidence-bar">
          <div 
            className="confidence-fill"
            style={{ width: `${result.confidence * 100}%` }}
          />
        </div>
      </div>

      <div className="all-predictions">
        <h3>Top 5 Predictions</h3>
        {sortedPredictions.map(([className, confidence], index) => (
          <div key={className} className="prediction-item">
            <div className="prediction-info">
              <span className="rank">#{index + 1}</span>
              <span className="class-name">
                {className.replace(/_/g, ' ').toUpperCase()}
              </span>
              <span className="percentage">
                {(confidence * 100).toFixed(2)}%
              </span>
            </div>
            <div className="progress-bar">
              <div 
                className="progress-fill"
                style={{ 
                  width: `${confidence * 100}%`,
                  backgroundColor: index === 0 ? '#10b981' : '#667eea'
                }}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ResultDisplay;
