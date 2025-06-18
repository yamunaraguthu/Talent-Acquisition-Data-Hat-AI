from fastapi import APIRouter, HTTPException
import httpx
from datetime import datetime
import os

router = APIRouter()

@router.get("/")
async def get_weather(city: str):
    api_key = os.getenv("WEATHERAPI_KEY") or "767c1905e7ab50e9f6751515fd1e7d46"
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
    
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail="Error fetching weather")
    
    data = resp.json()

    today = datetime.utcnow().strftime("%a %B %d %Y")

    temperature = data["main"]["temp"]
    main_weather = data["weather"][0]["main"]

    weather_data = [
        {
            "date": today,
            "main": main_weather,
            "temp": temperature
        }
    ]

    return {
        "count": len(weather_data),   # ✅ Added count
        "location": data.get("name"),
        "unit": "metric",
        "data": weather_data
    }