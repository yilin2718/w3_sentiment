from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
#https://pydantic-docs.helpmanual.io/usage/models/



app = FastAPI()
@app.get("/")
def hello_world():
    return {"Hello": "yi"}

from transformers import pipeline
import config

sentiment_model = pipeline("sentiment-analysis")

class PredictionRequest(BaseModel):
  query_string: str
  #query_string_list: List[str]  

@app.post("/new-sentiment")
async def analyze_sentiment(username: str, text: str):    
    user_inputted_sentiment = sentiment_model(text)
    return {f"USER: {username} TEXT: {text} SENTIMENT: {user_inputted_sentiment}"}


