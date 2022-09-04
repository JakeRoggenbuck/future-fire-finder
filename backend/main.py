from datetime import datetime
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

app = FastAPI()


class PredictionRequest(BaseModel):
    time_start: datetime
    time_end: datetime
    lat: float
    lon: float
    dataset: str


@app.get("/")
def read_root():
    return "Future Fire Finder"


@app.post("/predict")
def post_predict(prediction_request: PredictionRequest):
    return


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
