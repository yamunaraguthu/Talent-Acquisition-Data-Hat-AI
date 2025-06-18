from fastapi import APIRouter, Depends, HTTPException
from app.auth import oauth2_scheme
from jose import jwt, JWTError
import httpx
import os
from app.utils import SECRET_KEY, ALGORITHM

router = APIRouter()

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email = payload.get("sub")
        if user_email is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        return user_email
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.get("/")
async def get_news(search: str = None, user: str = Depends(get_current_user)):
    api_key = os.getenv("NEWSAPI_KEY") or "7b292e04a7ac4bb59f787de6e9fbed04"  # ideally load from env
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    if search:
        url += f"&q={search}"

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)

    print("NewsAPI response status:", resp.status_code)
    print("NewsAPI response body:", resp.text)

    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail="Error fetching news")

    news_data = resp.json()
    articles = news_data.get("articles", [])

    return {
        "count": len(articles),  # This adds the count
        "data": articles
    }