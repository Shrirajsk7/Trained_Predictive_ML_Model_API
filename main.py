from fastapi import FastAPI, Response, status, File, Form, UploadFile
from pydantic import BaseModel
import joblib

class Airflow(BaseModel):
    topic: str

app = FastAPI()

model = joblib.load("gradient_boosting.joblib")

@app.post("/api/volume_prediction")
async def predict_volume(vol_moving_avg: float = Form(), adj_close_rolling_med: float = Form()):
    features = [vol_moving_avg, adj_close_rolling_med]
    predicted_volume = model.predict([features])[0]
    return {"predicted_volume": predicted_volume}
