from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.post("/predict")
def predict(data: IrisInput):
    features = np.array([[data.sepal_length, data.sepal_width,
                          data.petal_length, data.petal_width]])
    prediction = model.predict(features)[0]
    classes = ["setosa", "versicolor", "virginica"]
    return {"prediction": classes[prediction]}
