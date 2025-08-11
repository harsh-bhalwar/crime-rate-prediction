from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
from typing import Optional

app = FastAPI(title="Crime Rate Prediction API")

# Load the models and encoder
try:
    random_forest = joblib.load("models/random_forest.pkl")
    xg_model = joblib.load("models/xgModel.pkl")
    knn_model = joblib.load("models/knnModel.pkl")
    city_encoder = joblib.load("models/city_encoder.pkl")
    knn_features = joblib.load("models/knnFeatures.pkl")
except Exception as e:
    print(f"Error loading models: {str(e)}")
    raise

class CrimeData(BaseModel):
    City: str
    ARSON: int
    ASSAULT: int
    BURGLARY: int
    COUNTERFEITING: int
    CYBERCRIME: int
    DRUG_OFFENSE: int
    EXTORTION: int
    FIREARM_OFFENSE: int
    FRAUD: int
    ROBBERY: int
    SHOPLIFTING: int
    TRAFFIC_VIOLATION: int
    VANDALISM: int
    VEHICLE_THEFT: int
    Population: int
    Unemployment_Rate: float
    Literacy_Rate: float
    Total_Crimes: int

@app.post("/predict")
async def predict_crime_rate(data: CrimeData):
    try:
        # Convert input data to DataFrame
        input_data = pd.DataFrame([{
            'City': data.City,
            'ARSON': data.ARSON,
            'ASSAULT': data.ASSAULT,
            'BURGLARY': data.BURGLARY,
            'COUNTERFEITING': data.COUNTERFEITING,
            'CYBERCRIME': data.CYBERCRIME,
            'DRUG OFFENSE': data.DRUG_OFFENSE,
            'EXTORTION': data.EXTORTION,
            'FIREARM OFFENSE': data.FIREARM_OFFENSE,
            'FRAUD': data.FRAUD,
            'ROBBERY': data.ROBBERY,
            'SHOPLIFTING': data.SHOPLIFTING,
            'TRAFFIC VIOLATION': data.TRAFFIC_VIOLATION,
            'VANDALISM': data.VANDALISM,
            'VEHICLE THEFT': data.VEHICLE_THEFT,
            'Population': data.Population,
            'Unemployment Rate': data.Unemployment_Rate,
            'Literacy Rate': data.Literacy_Rate,
            'Total Crimes': data.Total_Crimes
        }])

        # Encode city
        encoded_city = city_encoder.transform(input_data[['City']])
        encoded_city_df = pd.DataFrame(
            encoded_city, 
            columns=city_encoder.get_feature_names_out(['City'])
        )

        # Prepare features for Random Forest and XGBoost
        X_new = pd.concat([encoded_city_df, input_data.drop(['City'], axis=1)], axis=1)
        
        # Ensure all columns match training order for Random Forest
        missing_cols = set(random_forest.feature_names_in_) - set(X_new.columns)
        for col in missing_cols:
            X_new[col] = 0
        X_new = X_new[random_forest.feature_names_in_]

        # Make predictions
        rf_pred = float(random_forest.predict(X_new)[0])
        xgb_pred = float(xg_model.predict(X_new)[0])
        
        # Prepare features for KNN
        X_knn = pd.concat([encoded_city_df, input_data.drop(['City'], axis=1)], axis=1)
        missing_cols_knn = set(knn_features) - set(X_knn.columns)
        for col in missing_cols_knn:
            X_knn[col] = 0
        X_knn = X_knn[knn_features]
        knn_pred = float(knn_model.predict(X_knn)[0])

        # Calculate ensemble prediction (average of all models)
        ensemble_prediction = (rf_pred + xgb_pred + knn_pred) / 3

        return {
            "random_forest_prediction": round(rf_pred, 2),
            "xgboost_prediction": round(xgb_pred, 2),
            "knn_prediction": round(knn_pred, 2),
            "ensemble_prediction": round(ensemble_prediction, 2)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to the Crime Rate Prediction API"} 