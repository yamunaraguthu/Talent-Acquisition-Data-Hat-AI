from fastapi import FastAPI
from app import auth, news, weather
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="News & Weather Aggregator", version="1.0")

@app.get("/")
def root():
    return {"message": "Welcome to News & Weather API"}

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(news.router, prefix="/news", tags=["News"])
app.include_router(weather.router, prefix="/weather", tags=["Weather"])