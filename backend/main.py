from datetime import datetime
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

app = FastAPI()


class PredictionRequest(BaseModel):
    single_time: datetime
    lat: float
    lon: float


@app.get("/")
def read_root():
    return "Future Fire Finder"


@app.post("/predict")
def post_predict(prediction_request: PredictionRequest):
    return prediction_request


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
