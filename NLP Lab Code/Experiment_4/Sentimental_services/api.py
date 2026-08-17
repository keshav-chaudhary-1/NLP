from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_sentiment


app = FastAPI()


class TextInput(BaseModel):
    text: str


@app.get("/")
def home():

    return {
        "message": "Sentiment Analysis API is running"
    }


@app.post("/predict")
def predict(data: TextInput):

    result = predict_sentiment(data.text)

    return result