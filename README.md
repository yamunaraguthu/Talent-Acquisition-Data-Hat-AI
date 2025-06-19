# Talent-Acquisition-Data-Hat-AI

Data-Hat FastAPI Backed for News & Weather Aggregation 

This is a FastAPI backend application for news and weather aggregation, developed as part of the Data-Hat Full Stack Developer Assignment. The backend provides authenticated access to news data and unauthenticated access to weather data, aggregating information from third-party APIs.

🚀 Features

User authentication (signup, login, logout) using JWT tokens

News aggregation (requires authentication) via NewsAPI

Weather data aggregation (no authentication needed)

Swagger documentation available at /docs

Caching to reduce load on third-party APIs

---

🛠 Tech Stack

Python 

FastAPI

JWT for authentication

NewsAPI / OpenWeatherMap (or similar)

---
⚡ Setup & Installation

1️⃣ Clone the repository

git clone https://github.com/your-username/data-hat-backend.git
cd data-hat-backend

2️⃣ Create a virtual environment

python -m venv yamuna
yamuna\Scripts\activate     

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Set up environment variables

Create a .env file based on .env.example:

SECRET_KEY=your-secret-key
NEWS_API_KEY=your-news-api-key
WEATHER_API_KEY=your-weather-api-key


5️⃣ Run the app

uvicorn app.main:app --reload

---

📌 Authentication Endpoints

POST /signup — Register a new user

POST /login — Login and receive JWT token

POST /logout — Invalidate token

---
📌 News Endpoints

Route:GET/news
Description:Fetches top headlines or search-based news using NewsAPI
query Param:Search(Optional)

---

📝 Example Responses

Weather
{
  "count": 1,
  "location": "Srikakulam",
  "unit": "metric",
  "data": [
    {
      "date": "Thu June 19 2025",
      "main": "Clouds",
      "temp": 28.13
    }
  ]

---

🌟 Nice to Have

✅ Rate-limiting
✅ Token refresh mechanism
✅ Dockerization
✅ CI/CD pipeline
✅ Multi-city weather support
✅ redis caching

---

📤 Submission

Please push your code to GitHub and share with: saksham@data-hat.com.
Ensure you include:

✅ Codebase

✅ README.md

✅ .env.example

🔁 (Optional) Postman or Swagger export


