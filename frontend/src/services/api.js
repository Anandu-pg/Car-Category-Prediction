import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

/**
 * Predict vehicle category from image
 * @param {File} imageFile - Image file to classify
 * @returns {Promise} Prediction results
 */
export const predictVehicle = async (imageFile) => {
  const formData = new FormData();
  formData.append('file', imageFile);

  try {
    const response = await axios.post(`${API_BASE_URL}/predict`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error) {
    if (error.response) {
      throw error.response.data;
    }
    throw new Error('Network error. Please check if backend is running.');
  }
};

/**
 * Check API health status
 * @returns {Promise} Health status
 */
export const checkHealth = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/health`);
    return response.data;
  } catch (error) {
    throw new Error('Cannot connect to backend');
  }
};

/**
 * Get all supported vehicle classes
 * @returns {Promise} List of classes
 */
export const getClasses = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/classes`);
    return response.data;
  } catch (error) {
    throw new Error('Failed to fetch classes');
  }
};
