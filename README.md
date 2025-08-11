# 🚨 Crime Rate Prediction API

A machine learning-powered API that predicts crime rates using an ensemble of Random Forest, XGBoost, and K-Nearest Neighbors algorithms. This project provides accurate crime rate predictions based on various demographic and crime-related features.

## 🚀 Features

- **Ensemble Learning**: Combines predictions from three different ML models for improved accuracy
- **FastAPI Backend**: Modern, fast, and auto-documenting REST API
- **Multiple Models**: Random Forest, XGBoost, and KNN algorithms
- **City Encoding**: Handles categorical city data efficiently
- **Real-time Predictions**: Instant crime rate predictions via HTTP endpoints
- **Interactive Documentation**: Built-in Swagger UI and ReDoc

## 📊 Model Performance

The ensemble approach combines the strengths of multiple algorithms:
- **Random Forest**: Robust handling of non-linear relationships
- **XGBoost**: High performance with gradient boosting
- **KNN**: Effective for pattern recognition in similar cases

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/crime-rate-prediction.git
   cd crime-rate-prediction
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download model files**
   Ensure all model files are in the `models/` directory:
   - `random_forest.pkl`
   - `xgModel.pkl`
   - `knnModel.pkl`
   - `city_encoder.pkl`
   - `knnFeatures.pkl`

5. **Run the application**
   ```bash
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

The API will be available at `http://localhost:8000`

## 📖 API Usage

### Endpoints

#### GET `/`
Welcome message and API information.

#### POST `/predict`
Predicts crime rate based on input features.

### Request Format

```json
{
  "City": "Metropolis",
  "ARSON": 10,
  "ASSAULT": 85,
  "BURGLARY": 120,
  "COUNTERFEITING": 5,
  "CYBERCRIME": 40,
  "DRUG_OFFENSE": 70,
  "EXTORTION": 3,
  "FIREARM_OFFENSE": 12,
  "FRAUD": 30,
  "ROBBERY": 25,
  "SHOPLIFTING": 55,
  "TRAFFIC_VIOLATION": 200,
  "VANDALISM": 35,
  "VEHICLE_THEFT": 28,
  "Population": 500000,
  "Unemployment_Rate": 6.5,
  "Literacy_Rate": 92.3,
  "Total_Crimes": 718
}
```

### Response Format

```json
{
  "random_forest_prediction": 29.34,
  "xgboost_prediction": 30.95,
  "knn_prediction": 28.67,
  "ensemble_prediction": 29.65
}
```

## 🔧 API Documentation

Once the server is running, access the interactive documentation:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 📁 Project Structure

```
crime-rate-prediction/
├── app.py                 # FastAPI application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Git ignore file
├── LICENSE               # Project license
├── models/               # Trained model files
│   ├── random_forest.pkl
│   ├── xgModel.pkl
│   ├── knnModel.pkl
│   ├── city_encoder.pkl
│   └── knnFeatures.pkl
├── notebooks/            # Jupyter notebooks
│   ├── random_forest.ipynb
│   ├── xgBoost.ipynb
│   ├── Knn.ipynb
│   └── model2.ipynb
└── docs/                 # Additional documentation
    └── api_guide.md
```

## 🧪 Testing the API

### Using curl
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "City": "Metropolis",
       "ARSON": 10,
       "ASSAULT": 85,
       "BURGLARY": 120,
       "COUNTERFEITING": 5,
       "CYBERCRIME": 40,
       "DRUG_OFFENSE": 70,
       "EXTORTION": 3,
       "FIREARM_OFFENSE": 12,
       "FRAUD": 30,
       "ROBBERY": 25,
       "SHOPLIFTING": 55,
       "TRAFFIC_VIOLATION": 200,
       "VANDALISM": 35,
       "VEHICLE_THEFT": 28,
       "Population": 500000,
       "Unemployment_Rate": 6.5,
       "Literacy_Rate": 92.3,
       "Total_Crimes": 718
     }'
```

### Using Python requests
```python
import requests
import json

url = "http://localhost:8000/predict"
data = {
    "City": "Metropolis",
    "ARSON": 10,
    "ASSAULT": 85,
    # ... other features
}

response = requests.post(url, json=data)
print(response.json())
```

## 🚀 Deployment

### Local Development
```bash
uvicorn app:app --reload
```

### Production
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

### Docker (recommended for production)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- Scikit-learn for machine learning tools
- XGBoost for gradient boosting implementation
- Joblib for model serialization

## 📞 Support

If you have any questions or need help:
- Open an issue on GitHub
- Contact: bhalwar14harsh05@gmail.com
- Project Link: [https://github.com/harsh-bhalware/crime-rate-prediction](https://github.com/harsh-bhalwar/crime-rate-prediction)

---

⭐ **Star this repository if you find it helpful!** 
