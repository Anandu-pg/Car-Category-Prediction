import React, { useState, useEffect } from 'react';
import PredictionForm from './components/PredictionForm';
import ResultDisplay from './components/ResultDisplay';
import { predictVehicle, checkHealth } from './services/api';
import './App.css';

function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [apiStatus, setApiStatus] = useState('checking');

  // Check API health on component mount
  useEffect(() => {
    const checkApiHealth = async () => {
      try {
        await checkHealth();
        setApiStatus('connected');
      } catch (err) {
        setApiStatus('disconnected');
        console.error('API health check failed:', err);
      }
    };

    checkApiHealth();
    
    // Check every 30 seconds
    const interval = setInterval(checkApiHealth, 30000);
    return () => clearInterval(interval);
  }, []);

  const handlePredict = async (imageFile) => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const prediction = await predictVehicle(imageFile);
      setResult(prediction);
    } catch (err) {
      const errorMessage = err.detail || err.message || 'Prediction failed. Please try again.';
      setError(errorMessage);
      console.error('Prediction error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🚗 Vehicle Category Prediction</h1>
        <p className="subtitle">
          AI-powered vehicle classification using Deep Learning
        </p>
        <div className={`api-status api-status-${apiStatus}`}>
          <span className="status-dot"></span>
          API Status: {apiStatus === 'connected' ? 'Connected' : apiStatus === 'disconnected' ? 'Disconnected' : 'Checking...'}
        </div>
      </header>

      <main className="App-main">
        <div className="container">
          <PredictionForm onPredict={handlePredict} loading={loading} />
          
          {error && (
            <div className="error-message">
              <h3>❌ Error</h3>
              <p>{error}</p>
            </div>
          )}

          {result && <ResultDisplay result={result} />}
        </div>
      </main>

      <footer className="App-footer">
        <p>
          Powered by <strong>FastAPI</strong> & <strong>React</strong> | 
          Model: <strong>InceptionV3</strong>
        </p>
      </footer>
    </div>
  );
}

export default App;
