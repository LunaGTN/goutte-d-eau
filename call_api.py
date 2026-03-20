
from fastapi import FastAPI
from main import predict_rain_with_date



#MON_API
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "API qui renvoie une probabilité de pluie"}

@app.get("/predict/")
async def predict_rain(date):
    return {"rain_probability": predict_rain_with_date(date)}


